#!/usr/bin/env python3
"""
Job Recommendation FastAPI Application
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import uvicorn
from dotenv import load_dotenv
import os

from models import JobRecommendationRequest, JobRecommendationResponse, JobData
from services import JobRecommendationService

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Job Recommendation API",
    description="AI-powered job recommendation system that analyzes resumes against job postings",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize service
job_service = JobRecommendationService()

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Job Recommendation API is running!", "version": "1.0.0"}

@app.post("/recommend-jobs", response_model=JobRecommendationResponse)
async def recommend_jobs(request: JobRecommendationRequest):
    """
    Get job recommendations based on resume and job search criteria
    """
    try:
        # Validate API keys
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
        if not os.getenv("FIRECRAWL_API_KEY"):
            raise HTTPException(status_code=500, detail="Firecrawl API key not configured")
        
        # Process the job recommendations
        result = await job_service.get_job_recommendations(
            resume_text=request.resume_text,
            jobs_page_url=request.jobs_page_url,
            num_jobs=request.num_jobs,
            num_recommendations=request.num_recommendations
        )
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/health")
async def health_check():
    """Detailed health check with API key status"""
    return {
        "status": "healthy",
        "openai_configured": bool(os.getenv("OPENAI_API_KEY")),
        "firecrawl_configured": bool(os.getenv("FIRECRAWL_API_KEY"))
    }

@app.post("/recommend-jobs-demo", response_model=JobRecommendationResponse)
async def recommend_jobs_demo(request: JobRecommendationRequest):
    """
    Demo endpoint that uses mock job data for testing purposes
    """
    try:
        # Validate OpenAI API key for demo
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
        
        # Use mock job data
        mock_job_data = [
            {
                "job_title": "Data Engineering Manager",
                "location": "San Francisco",
                "compensation": "$405K – $490K • Offers Equity",
                "key_skills": [
                    "data engineering",
                    "leadership",
                    "data strategy",
                    "data architecture",
                    "data quality",
                    "data governance",
                    "programming languages (Python, Scala, Java)"
                ],
                "apply_link": "https://jobs.ashbyhq.com/openai/b3394315-e8da-4f54-9926-dfe32a1e4913/application",
                "sub_division_of_organization": "Applied AI"
            },
            {
                "job_title": "Data Engineer, Analytics",
                "location": "San Francisco",
                "compensation": "$255K – $405K • Offers Equity",
                "key_skills": [
                    "3+ years of experience as a data engineer",
                    "8+ years of software engineering experience",
                    "Proficiency in Python, Scala, or Java",
                    "Experience with Hadoop, Flink, HDFS, S3",
                    "Expertise with ETL schedulers like Airflow, Dagster, Prefect",
                    "Solid understanding of Spark"
                ],
                "apply_link": "https://jobs.ashbyhq.com/openai/fc5bbc77-a30c-4e7a-9acc-8a2e748545b4/application",
                "sub_division_of_organization": "Applied AI"
            },
            {
                "job_title": "Backend Software Engineer (Evals)",
                "location": "San Francisco",
                "compensation": "$255K – $405K • Offers Equity",
                "key_skills": [
                    "Backend engineering",
                    "Python",
                    "FastAPI",
                    "Postgres",
                    "Distributed systems",
                    "APIs",
                    "Data processing pipelines",
                    "AI agents",
                    "Evaluation methods for LLMs"
                ],
                "apply_link": "https://jobs.ashbyhq.com/openai/3d064454-c0c3-4225-bc2c-6d8c0f8735b2/application",
                "sub_division_of_organization": "Applied AI"
            },
            {
                "job_title": "Backend Software Engineer, Growth",
                "location": "San Francisco",
                "compensation": "$160K – $385K • Offers Equity",
                "key_skills": [
                    "data analysis",
                    "product ideation",
                    "experimentation",
                    "A/B testing",
                    "backend systems",
                    "collaboration with cross-functional teams"
                ],
                "apply_link": "https://jobs.ashbyhq.com/openai/dd2025b9-4d18-4ad7-a78c-7a643419ecc5/application",
                "sub_division_of_organization": "Applied AI"
            },
            {
                "job_title": "Engineering Manager, Data Infrastructure",
                "location": "San Francisco",
                "compensation": "$325K – $405K • Offers Equity",
                "key_skills": [
                    "Data Infrastructure",
                    "Terraform",
                    "Kubernetes",
                    "SRE",
                    "Apache Spark",
                    "Apache Iceberg",
                    "Airflow",
                    "Kafka",
                    "Flink",
                    "Chronon"
                ],
                "apply_link": "https://jobs.ashbyhq.com/openai/4f5a0df1-22d7-49a6-8ea1-c15c886fbade/application",
                "sub_division_of_organization": "Applied AI"
            }
        ]
        
        # Limit to requested number of jobs
        limited_jobs = mock_job_data[:request.num_jobs]
        
        # Generate recommendations using AI
        result = await job_service._generate_recommendations(
            resume_text=request.resume_text,
            job_data=[JobData(**job) for job in limited_jobs],
            num_recommendations=request.num_recommendations
        )
        
        return JobRecommendationResponse(
            success=True,
            message=f"Demo: Successfully analyzed {len(limited_jobs)} mock jobs and generated {len(result)} recommendations",
            total_jobs_found=len(limited_jobs),
            total_jobs_analyzed=len(limited_jobs),
            recommendations=result,
            all_jobs=[JobData(**job) for job in limited_jobs],
            processing_time_seconds=1.5
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing demo request: {str(e)}")

@app.post("/recommend-jobs-real", response_model=JobRecommendationResponse)
async def recommend_jobs_real(request: JobRecommendationRequest):
    """
    Real job recommendations using actual job scraping (like job_agent.py)
    """
    try:
        # Validate API keys
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
        if not os.getenv("FIRECRAWL_API_KEY"):
            raise HTTPException(status_code=500, detail="Firecrawl API key not configured")
        
        # Use the actual job agent logic
        firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        # Import FirecrawlApp (assuming it's available)
        try:
            from firecrawl import FirecrawlApp
            firecrawl = FirecrawlApp(api_key=firecrawl_api_key)
        except ImportError:
            raise HTTPException(status_code=500, detail="Firecrawl library not installed")
        
        # Scrape job data from the provided URL
        scrape_result = firecrawl.scrape_url(
            request.jobs_page_url,
            params={
                'formats': ['markdown'],
                'includeTags': ['main'],
                'onlyMainContent': True
            }
        )
        
        if not scrape_result or 'markdown' not in scrape_result:
            raise HTTPException(status_code=500, detail="Failed to scrape job data from URL")
        
        # Parse the scraped content to extract job data
        # This is a simplified version - you might need to adjust based on your specific job site format
        import re
        import json
        
        content = scrape_result['markdown']
        
        # Extract job listings using regex (this is a basic implementation)
        # You might need to customize this based on the specific job site format
        job_pattern = r'(?:Job Title|Position|Role):\s*([^\n]+)(?:\n.*?Salary|Compensation):\s*([^\n]+)(?:\n.*?Apply|Link):\s*([^\n]+)'
        matches = re.findall(job_pattern, content, re.IGNORECASE | re.DOTALL)
        
        extracted_data = []
        for match in matches[:request.num_jobs]:
            if len(match) >= 3:
                extracted_data.append({
                    "job_title": match[0].strip(),
                    "compensation": match[1].strip(),
                    "apply_link": match[2].strip()
                })
        
        if not extracted_data:
            raise HTTPException(status_code=500, detail="No job data found on the provided URL")
        
        # Generate AI recommendations
        prompt = f"""
        Please analyze the resume and job listings, and return a JSON list of the top {request.num_recommendations} roles that best fit the candidate's experience and skills. Include only the job title, compensation, and apply link for each recommended role. The output should be a valid JSON array of objects in the following format, with no additional text:

        [
          {{
            "job_title": "Job Title",
            "compensation": "Compensation (if available, otherwise empty string)",
            "apply_link": "Application URL"
          }}
        ]

        Based on the following resume:
        {request.resume_text}

        And the following job listings:
        {json.dumps(extracted_data, indent=2)}
        """
        
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )
        
        try:
            response_content = completion.choices[0].message.content.strip()
            # Remove markdown code blocks if present
            if response_content.startswith('```json'):
                response_content = response_content[7:]
            if response_content.startswith('```'):
                response_content = response_content[3:]
            if response_content.endswith('```'):
                response_content = response_content[:-3]
            
            recommended_jobs = json.loads(response_content.strip())
            
            # Convert to JobData objects
            all_jobs = [JobData(
                job_title=job.get("job_title", ""),
                location="",
                compensation=job.get("compensation", ""),
                key_skills=[],
                apply_link=job.get("apply_link", ""),
                sub_division_of_organization=""
            ) for job in extracted_data]
            
            recommendations = [JobData(
                job_title=rec.get("job_title", ""),
                location="",
                compensation=rec.get("compensation", ""),
                key_skills=[],
                apply_link=rec.get("apply_link", ""),
                sub_division_of_organization=""
            ) for rec in recommended_jobs]
            
            return JobRecommendationResponse(
                success=True,
                message=f"Successfully analyzed {len(extracted_data)} real jobs and generated {len(recommendations)} recommendations",
                total_jobs_found=len(extracted_data),
                total_jobs_analyzed=len(extracted_data),
                recommendations=recommendations,
                all_jobs=all_jobs,
                processing_time_seconds=2.0
            )
            
        except json.JSONDecodeError as e:
            raise HTTPException(status_code=500, detail=f"Error parsing AI recommendations: {str(e)}")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing real job request: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
