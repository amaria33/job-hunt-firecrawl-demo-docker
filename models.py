"""
Pydantic models for the Job Recommendation API
"""

from pydantic import BaseModel, Field, validator
from typing import List, Optional

class JobRecommendationRequest(BaseModel):
    """Request model for job recommendations"""
    resume_text: str = Field(..., description="Resume text content", min_length=100)
    jobs_page_url: Optional[str] = Field(
        default="https://jobs.ashbyhq.com/openai",
        description="URL of the jobs page to scrape"
    )
    num_jobs: int = Field(
        default=5,
        description="Number of jobs to extract and analyze",
        ge=1,
        le=20
    )
    num_recommendations: int = Field(
        default=3,
        description="Number of top recommendations to return",
        ge=1,
        le=10
    )
    
    @validator('jobs_page_url')
    def validate_url(cls, v):
        if v and not v.startswith(('http://', 'https://')):
            raise ValueError('URL must start with http:// or https://')
        return v

class JobData(BaseModel):
    """Model for individual job data"""
    job_title: str = Field(..., description="Job title")
    location: str = Field(..., description="Job location")
    compensation: str = Field(..., description="Salary/compensation information")
    key_skills: List[str] = Field(..., description="Required skills for the job")
    apply_link: str = Field(..., description="URL to apply for the job")
    sub_division_of_organization: Optional[str] = Field(None, description="Department or division")

class JobRecommendation(BaseModel):
    """Model for job recommendations"""
    job_title: str = Field(..., description="Recommended job title")
    compensation: str = Field(..., description="Compensation information")
    apply_link: str = Field(..., description="Application URL")
    match_reason: Optional[str] = Field(None, description="Why this job matches the candidate")

class JobRecommendationResponse(BaseModel):
    """Response model for job recommendations"""
    success: bool = Field(..., description="Whether the operation was successful")
    message: str = Field(..., description="Status message")
    total_jobs_found: int = Field(..., description="Total number of jobs extracted")
    total_jobs_analyzed: int = Field(..., description="Number of jobs successfully analyzed")
    recommendations: List[JobRecommendation] = Field(..., description="Top job recommendations")
    all_jobs: Optional[List[JobData]] = Field(None, description="All jobs that were analyzed")
    processing_time_seconds: Optional[float] = Field(None, description="Time taken to process the request")
