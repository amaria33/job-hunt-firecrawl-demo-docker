# Job Recommendation FastAPI Application

A FastAPI-based job recommendation system that analyzes resumes against job postings and provides personalized recommendations.

## Features

- 🎯 **AI-Powered Analysis**: Uses OpenAI GPT-4 to match resumes with job requirements
- 🌐 **Web Scraping**: Extracts job data from various job boards using Firecrawl
- ⚡ **FastAPI**: High-performance async API with automatic documentation
- 🔧 **Configurable**: Customizable number of jobs to analyze and recommendations to return
- 📊 **Detailed Responses**: Comprehensive job data and match explanations

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Variables

Create a `.env` file with your API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
```

### 3. Run the Application

```bash
python app.py
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, visit:
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### POST `/recommend-jobs`

Get job recommendations based on resume analysis.

**Request Body:**
```json
{
  "resume_text": "Your complete resume text here...",
  "jobs_page_url": "https://jobs.ashbyhq.com/openai",
  "num_jobs": 5,
  "num_recommendations": 3
}
```

**Response:**
```json
{
  "success": true,
  "message": "Successfully analyzed 5 jobs and generated 3 recommendations",
  "total_jobs_found": 5,
  "total_jobs_analyzed": 5,
  "recommendations": [
    {
      "job_title": "Data Engineering Manager",
      "compensation": "$405K – $490K • Offers Equity",
      "apply_link": "https://jobs.ashbyhq.com/openai/...",
      "match_reason": "Matches your experience with data management and leadership"
    }
  ],
  "all_jobs": [...],
  "processing_time_seconds": 45.2
}
```

### GET `/health`

Check API health and configuration status.

### GET `/`

Basic health check endpoint.

## Parameters

- **resume_text** (required): Your complete resume text (minimum 100 characters)
- **jobs_page_url** (optional): URL to scrape jobs from (default: https://jobs.ashbyhq.com/openai)
- **num_jobs** (optional): Number of jobs to extract and analyze (1-20, default: 5)
- **num_recommendations** (optional): Number of top recommendations to return (1-10, default: 3)

## Testing

Run the test script to verify the API:

```bash
python test_api.py
```

## Example Usage

### Using curl:

```bash
curl -X POST "http://localhost:8000/recommend-jobs" \
     -H "Content-Type: application/json" \
     -d '{
       "resume_text": "Your resume text here...",
       "num_jobs": 3,
       "num_recommendations": 2
     }'
```

### Using Python requests:

```python
import requests

response = requests.post(
    "http://localhost:8000/recommend-jobs",
    json={
        "resume_text": "Your resume text here...",
        "jobs_page_url": "https://jobs.ashbyhq.com/openai",
        "num_jobs": 5,
        "num_recommendations": 3
    }
)

result = response.json()
print(result['recommendations'])
```

## Error Handling

The API includes comprehensive error handling:

- **Validation Errors**: Invalid input parameters
- **API Key Errors**: Missing or invalid API keys
- **Scraping Errors**: Issues with job page scraping
- **Rate Limiting**: Firecrawl API rate limits
- **Timeout Errors**: Request timeouts

## Production Deployment

For production deployment:

1. Set up proper CORS origins in `app.py`
2. Use environment variables for configuration
3. Consider using a reverse proxy (nginx)
4. Set up monitoring and logging
5. Use a production ASGI server like Gunicorn

```bash
pip install gunicorn
gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```
