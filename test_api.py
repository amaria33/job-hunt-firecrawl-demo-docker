#!/usr/bin/env python3
"""
Test script for the Job Recommendation API
"""

import requests
import json
import sys
import time
from typing import Dict, Any

# API base URL
BASE_URL = "http://localhost:8000"

def check_server_running() -> bool:
    """Check if the API server is running"""
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# Sample resume data (you can replace this with actual resume text)
SAMPLE_RESUME = """
R. Ashley Maria, MBA, M.Ed.
Kansas City, KS • +1 (806) 220-3562 • ralucero@me.com

PROFESSIONAL PROFILE:
Detail-oriented and solutions-driven human resources professional with a strong foundation in regulatory compliance, cybersecurity awareness, and system optimization, seeking to leverage expertise in risk mitigation, secure process design, and cross-functional collaboration to support enterprise-wide security and compliance initiatives within a dynamic organization.

KEY SKILLS:
CRM Software Management | Targeted Student Engagement | Digital Media Content Creation | Public Affairs Strategies | Event Coordination | Cybersecurity Awareness | Program Development | Digital Communication | Budget Management | Community Partnership Development | Financial Management | Educational Program Integration | Financial Literacy Programs | Data Security 

PROFESSIONAL EXPERIENCE:
HRIS Analyst | Unified Government of Wyandotte County, Kansas City, KS | June 2024 – Present
• System Leadership & Workday Optimization: Led the end-to-end refinement of Workday modules including Absence, HCM, Compensation, Recruiting, and LMS to align functionality with organizational strategy.
• Union Leave Plan Administration & Compliance Control: Managed complex structures for 13 bargaining units by configuring accrual logic, entitlement tracking, and separation settlements.
• Cross-Functional Process Integration: Translated multifaceted operational needs into sustainable system solutions by collaborating with business units to implement scalable configurations.

Executive Assistant | Boys & Girls Club of America | Dec 2023 – Present
• Executive Calendar Oversight & Operational Flow: Directed the daily management of the CEO's high-volume schedule by orchestrating meetings, travel logistics, and shifting priorities in real time.
• Stakeholder Communication & Relationship Management: Served as the strategic liaison between the executive office and internal/external contacts.

EDUCATION:
Master of Education: School Counseling | A&M University
Master of Business Administration: Human Resource Management | Wayland Baptist University
Bachelor of Business Administration: Business Administration | Wayland Baptist University

TECHNICAL PROFICIENCY:
Security & Compliance: NIST Risk Management Framework (RMF), FISMA, HIPAA, FERPA, Security Awareness Training, Access Control Protocols, Policy Implementation
HRIS Systems: Workday (Absence, HCM, Compensation, LMS, Recruiting), Skyward, FLSA Compliance Tracking, Accrual & Leave Plan Configuration
CRM & Data Management: Salesforce, Microsoft Dynamics, Enrollment & Records Management, CRM Optimization, Data Integrity & Auditing
"""

def test_health_check():
    """Test the health check endpoint"""
    print("🔍 Testing health check endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=10)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            print(f"✅ Server is healthy!")
            print(f"   - OpenAI configured: {data.get('openai_configured', False)}")
            print(f"   - Firecrawl configured: {data.get('firecrawl_configured', False)}")
        else:
            print(f"❌ Health check failed: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to server: {str(e)}")
    print()

def test_root_endpoint():
    """Test the root endpoint"""
    print("🏠 Testing root endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=10)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
        else:
            print(f"❌ Root endpoint failed: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to root endpoint: {str(e)}")
    print()

def test_job_recommendations_demo():
    """Test the job recommendations demo endpoint"""
    print("🎯 Testing job recommendations DEMO endpoint...")
    
    payload = {
        "resume_text": SAMPLE_RESUME,
        "num_jobs": 5,
        "num_recommendations": 3
    }
    
    print("Sending request with payload:")
    print(f"- Number of jobs to analyze: {payload['num_jobs']}")
    print(f"- Number of recommendations: {payload['num_recommendations']}")
    print(f"- Using mock job data (demo mode)")
    print()
    
    try:
        response = requests.post(f"{BASE_URL}/recommend-jobs-demo", json=payload, timeout=60)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Success: {result['success']}")
            print(f"Message: {result['message']}")
            print(f"Total jobs found: {result['total_jobs_found']}")
            print(f"Total jobs analyzed: {result['total_jobs_analyzed']}")
            print(f"Processing time: {result.get('processing_time_seconds', 'N/A')} seconds")
            print()
            
            if result['recommendations']:
                print("🏆 TOP RECOMMENDATIONS:")
                for i, rec in enumerate(result['recommendations'], 1):
                    print(f"{i}. {rec['job_title']}")
                    print(f"   💰 Compensation: {rec['compensation']}")
                    print(f"   🔗 Apply: {rec['apply_link']}")
                    if rec.get('match_reason'):
                        print(f"   💡 Match reason: {rec['match_reason']}")
                    print()
            else:
                print("❌ No recommendations generated.")
        else:
            print(f"❌ Error: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error making request: {str(e)}")
    
    print()

def test_simple_demo():
    """Test with minimal parameters"""
    print("⚡ Testing simple demo with minimal parameters...")
    
    payload = {
        "resume_text": "Software Engineer with 5 years experience in Python, FastAPI, and data analysis. Strong background in system optimization, API development, and database management. Experienced in working with cross-functional teams and delivering scalable solutions.",
        "num_jobs": 2,
        "num_recommendations": 1
    }
    
    try:
        response = requests.post(f"{BASE_URL}/recommend-jobs-demo", json=payload, timeout=30)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Quick test successful!")
            print(f"Recommendations: {len(result.get('recommendations', []))}")
            if result.get('recommendations'):
                print(f"Top match: {result['recommendations'][0]['job_title']}")
        else:
            print(f"❌ Simple test failed: {response.text}")
    except Exception as e:
        print(f"❌ Simple test error: {str(e)}")
    print()

def test_job_recommendations():
    """Test the job recommendations endpoint (real scraping)"""
    print("🌐 Testing job recommendations endpoint (real scraping)...")
    
    payload = {
        "resume_text": SAMPLE_RESUME,
        "jobs_page_url": "https://jobs.ashbyhq.com/openai",
        "num_jobs": 3,
        "num_recommendations": 2
    }
    
    print("Sending request with payload:")
    print(f"- Jobs page URL: {payload['jobs_page_url']}")
    print(f"- Number of jobs to analyze: {payload['num_jobs']}")
    print(f"- Number of recommendations: {payload['num_recommendations']}")
    print()
    
    response = requests.post(f"{BASE_URL}/recommend-jobs", json=payload)
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"Success: {result['success']}")
        print(f"Message: {result['message']}")
        print(f"Total jobs found: {result['total_jobs_found']}")
        print(f"Total jobs analyzed: {result['total_jobs_analyzed']}")
        print(f"Processing time: {result.get('processing_time_seconds', 'N/A')} seconds")
        print()
        
        if result['recommendations']:
            print("🏆 TOP RECOMMENDATIONS:")
            for i, rec in enumerate(result['recommendations'], 1):
                print(f"{i}. {rec['job_title']}")
                print(f"   Compensation: {rec['compensation']}")
                print(f"   Apply: {rec['apply_link']}")
                if rec.get('match_reason'):
                    print(f"   Match reason: {rec['match_reason']}")
                print()
        else:
            print("No recommendations generated.")
    else:
        print(f"Error: {response.text}")
    
    print()

def test_with_different_parameters():
    """Test with different parameters"""
    print("🔄 Testing with different parameters...")
    
    payload = {
        "resume_text": SAMPLE_RESUME,
        "num_jobs": 3,
        "num_recommendations": 2
        # Using default jobs_page_url
    }
    
    print("Sending request with custom parameters:")
    print(f"- Number of jobs to analyze: {payload['num_jobs']}")
    print(f"- Number of recommendations: {payload['num_recommendations']}")
    print(f"- Using default jobs page URL")
    print()
    
    response = requests.post(f"{BASE_URL}/recommend-jobs", json=payload)
    
    if response.status_code == 200:
        result = response.json()
        print(f"Success: {result['success']}")
        print(f"Jobs analyzed: {result['total_jobs_analyzed']}")
        print(f"Recommendations: {len(result['recommendations'])}")
    else:
        print(f"Error: {response.text}")
    
    print()

def run_all_tests():
    """Run all tests"""
    print("🚀 Job Recommendation API Test Suite")
    print("=" * 50)
    print()
    
    # Check if server is running first
    if not check_server_running():
        print("❌ Server is not running!")
        print("Please start the server with: python app.py")
        print("Then run this test script again.")
        return False
    
    print("✅ Server is running, starting tests...")
    print()
    
    try:
        test_health_check()
        test_root_endpoint()
        test_simple_demo()
        test_job_recommendations_demo()
        test_job_recommendations()
        test_with_different_parameters()
        
        print("✅ All tests completed!")
        return True
        
    except Exception as e:
        print(f"❌ Error running tests: {str(e)}")
        return False

def run_demo_only():
    """Run only the demo test (recommended)"""
    print("🎯 Quick Demo Test")
    print("=" * 20)
    print()
    
    if not check_server_running():
        print("❌ Server is not running!")
        print("Please start the server with: python app.py")
        return False
    
    try:
        test_simple_demo()
        print("✅ Demo test completed!")
        return True
    except Exception as e:
        print(f"❌ Error running demo: {str(e)}")
        return False

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        run_demo_only()
    else:
        run_all_tests()
        
    print("\n📚 Additional Resources:")
    print("- API Documentation: http://localhost:8000/docs")
    print("- ReDoc: http://localhost:8000/redoc")
    print("- Health Check: http://localhost:8000/health")
    print("\n💡 Tips:")
    print("- Use 'python test_api.py --demo' for quick testing")
    print("- Use 'python test_api.py' for full test suite")
    print("- Demo endpoint always works (no Firecrawl credits needed)")
