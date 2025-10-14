#!/bin/bash

# Job Recommendation API - Example Usage Script

echo "🚀 Job Recommendation API Examples"
echo "=================================="

# Base URL
BASE_URL="http://localhost:8000"

echo ""
echo "1. Health Check"
echo "==============="
curl -s "$BASE_URL/health" | jq '.'

echo ""
echo "2. Demo Job Recommendations (using mock data)"
echo "============================================="
curl -X POST "$BASE_URL/recommend-jobs-demo" \
     -H "Content-Type: application/json" \
     -d '{
       "resume_text": "R. Ashley Maria, MBA, M.Ed. Detail-oriented and solutions-driven human resources professional with a strong foundation in regulatory compliance, cybersecurity awareness, and system optimization. Experienced in HRIS systems, Workday optimization, data management, and project leadership.",
       "num_jobs": 3,
       "num_recommendations": 2
     }' | jq '.'

echo ""
echo "3. Real Job Recommendations (scraping from web)"
echo "=============================================="
curl -X POST "$BASE_URL/recommend-jobs" \
     -H "Content-Type: application/json" \
     -d '{
       "resume_text": "R. Ashley Maria, MBA, M.Ed. Detail-oriented and solutions-driven human resources professional with a strong foundation in regulatory compliance, cybersecurity awareness, and system optimization. Experienced in HRIS systems, Workday optimization, data management, and project leadership.",
       "jobs_page_url": "https://jobs.ashbyhq.com/openai",
       "num_jobs": 5,
       "num_recommendations": 3
     }' | jq '.'

echo ""
echo "4. Custom Parameters Example"
echo "============================"
curl -X POST "$BASE_URL/recommend-jobs-demo" \
     -H "Content-Type: application/json" \
     -d '{
       "resume_text": "Software Engineer with 5 years experience in Python, FastAPI, and data analysis. Strong background in system optimization and team collaboration.",
       "num_jobs": 4,
       "num_recommendations": 2
     }' | jq '.recommendations[] | {job_title, compensation, match_reason}'

echo ""
echo "✅ Examples completed!"
echo ""
echo "📚 API Documentation:"
echo "- Interactive docs: $BASE_URL/docs"
echo "- ReDoc: $BASE_URL/redoc"
