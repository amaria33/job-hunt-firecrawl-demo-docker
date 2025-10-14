"""
Service layer for job recommendation functionality
"""

import os
import json
import time
import requests
from typing import List, Optional
from openai import OpenAI
from models import JobData, JobRecommendation, JobRecommendationResponse

class JobRecommendationService:
    """Service class for job recommendation operations"""
    
    def __init__(self):
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
    
    async def get_job_recommendations(
        self,
        resume_text: str,
        jobs_page_url: str,
        num_jobs: int,
        num_recommendations: int
    ) -> JobRecommendationResponse:
        """
        Main method to get job recommendations
        """
        start_time = time.time()
        
        try:
            # Step 1: Scrape jobs page and extract job links
            print(f"Scraping jobs from: {jobs_page_url}")
            job_links = await self._extract_job_links(jobs_page_url, num_jobs)
            
            if not job_links:
                return JobRecommendationResponse(
                    success=False,
                    message="No job links found on the provided page",
                    total_jobs_found=0,
                    total_jobs_analyzed=0,
                    recommendations=[]
                )
            
            # Step 2: Extract detailed job data from each link
            print(f"Extracting detailed data from {len(job_links)} job postings...")
            job_data = await self._extract_job_details(job_links)
            
            if not job_data:
                return JobRecommendationResponse(
                    success=False,
                    message="No job data could be extracted from the job links",
                    total_jobs_found=len(job_links),
                    total_jobs_analyzed=0,
                    recommendations=[]
                )
            
            # Step 3: Generate recommendations using AI
            print(f"Generating recommendations based on {len(job_data)} jobs...")
            recommendations = await self._generate_recommendations(
                resume_text, job_data, num_recommendations
            )
            
            processing_time = time.time() - start_time
            
            return JobRecommendationResponse(
                success=True,
                message=f"Successfully analyzed {len(job_data)} jobs and generated {len(recommendations)} recommendations",
                total_jobs_found=len(job_links),
                total_jobs_analyzed=len(job_data),
                recommendations=recommendations,
                all_jobs=job_data,
                processing_time_seconds=round(processing_time, 2)
            )
            
        except Exception as e:
            processing_time = time.time() - start_time
            return JobRecommendationResponse(
                success=False,
                message=f"Error processing request: {str(e)}",
                total_jobs_found=0,
                total_jobs_analyzed=0,
                recommendations=[],
                processing_time_seconds=round(processing_time, 2)
            )
    
    async def _extract_job_links(self, jobs_page_url: str, num_jobs: int) -> List[str]:
        """Extract job application links from the jobs page"""
        try:
            response = requests.post(
                "https://api.firecrawl.dev/v1/scrape",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.firecrawl_api_key}"
                },
                json={
                    "url": jobs_page_url,
                    "formats": ["markdown"],
                    "waitFor": 2000,
                    "timeout": 30000
                }
            )
            
            if response.status_code != 200:
                print(f"Error scraping jobs page: {response.status_code} - {response.text}")
                return []
            
            result = response.json()
            if not result.get('success'):
                print(f"Failed to scrape jobs page: {result.get('message', 'Unknown error')}")
                return []
            
            html_content = result['data']['markdown']
            
            # Use OpenAI to extract job links
            prompt = f"""
            Extract up to {num_jobs} job application links from the given markdown content.
            Return the result as a JSON object with a single key 'apply_links' containing an array of strings (the links).
            The output should be a valid JSON object, with no additional text.
            Do not include any JSON markdown formatting or code block indicators.
            Provide only the raw JSON object as the response.

            Example of the expected format:
            {{"apply_links": ["https://example.com/job1", "https://example.com/job2", ...]}}

            Markdown content:
            {html_content[:50000]}
            """
            
            completion = self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            
            if completion.choices:
                response_content = completion.choices[0].message.content.strip()
                try:
                    result = json.loads(response_content)
                    return result.get('apply_links', [])
                except json.JSONDecodeError as e:
                    print(f"Error parsing job links JSON: {str(e)}")
                    return []
            
            return []
            
        except Exception as e:
            print(f"Error extracting job links: {str(e)}")
            return []
    
    async def _extract_job_details(self, job_links: List[str]) -> List[JobData]:
        """Extract detailed job information from each job link"""
        job_data = []
        
        for index, link in enumerate(job_links):
            try:
                response = requests.post(
                    "https://api.firecrawl.dev/v1/scrape",
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {self.firecrawl_api_key}"
                    },
                    json={
                        "url": link,
                        "formats": ["extract"],
                        "actions": [{
                            "type": "click",
                            "selector": "#job-overview"
                        }],
                        "extract": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "job_title": {"type": "string"},
                                    "sub_division_of_organization": {"type": "string"},
                                    "key_skills": {"type": "array", "items": {"type": "string"}},
                                    "compensation": {"type": "string"},
                                    "location": {"type": "string"},
                                    "apply_link": {"type": "string"}
                                },
                                "required": ["job_title", "sub_division_of_organization", "key_skills", "compensation", "location", "apply_link"]
                            }
                        }
                    }
                )
                
                if response.status_code == 200:
                    result = response.json()
                    if result.get('success'):
                        job_info = result['data']['extract']
                        job_data.append(JobData(**job_info))
                        print(f"✓ Extracted data for job {index + 1}/{len(job_links)}")
                    else:
                        print(f"✗ Failed to extract data for job {index + 1}: {result.get('message', 'Unknown error')}")
                else:
                    print(f"✗ Error {response.status_code} for job {index + 1}")
                    
            except Exception as e:
                print(f"✗ Exception for job {index + 1}: {str(e)[:100]}...")
        
        return job_data
    
    async def _generate_recommendations(
        self,
        resume_text: str,
        job_data: List[JobData],
        num_recommendations: int
    ) -> List[JobRecommendation]:
        """Generate job recommendations using AI analysis"""
        
        # Convert job data to dict for JSON serialization
        jobs_dict = [job.dict() for job in job_data]
        
        prompt = f"""
        Please analyze the resume and job listings, and return a JSON list of the top {num_recommendations} roles that best fit the candidate's experience and skills. 
        Include only the job title, compensation, and apply link for each recommended role. 
        The output should be a valid JSON array of objects in the following format, with no additional text:

        [
          {{
            "job_title": "Job Title",
            "compensation": "Compensation (if available, otherwise empty string)",
            "apply_link": "Application URL",
            "match_reason": "Brief explanation of why this job matches the candidate's background"
          }},
          ...
        ]

        Based on the following resume:
        {resume_text}

        And the following job listings:
        {json.dumps(jobs_dict, indent=2)}
        """
        
        try:
            completion = self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_content = completion.choices[0].message.content.strip()
            
            # Remove markdown code blocks if present
            if response_content.startswith('```json'):
                response_content = response_content[7:]
            if response_content.startswith('```'):
                response_content = response_content[3:]
            if response_content.endswith('```'):
                response_content = response_content[:-3]
            
            recommendations_data = json.loads(response_content.strip())
            
            return [JobRecommendation(**rec) for rec in recommendations_data]
            
        except json.JSONDecodeError as e:
            print(f"Error parsing recommendations JSON: {str(e)}")
            return []
        except Exception as e:
            print(f"Error generating recommendations: {str(e)}")
            return []
