#!/usr/bin/env python3
"""
Job Recommendation Agent - Demo Version
This version uses mock data to demonstrate the functionality
"""

import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# ANSI color codes
class Colors:
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

# Load environment variables
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Resume
resume_paste = """"
R. Ashley Maria, MBA, M.Ed.
Kansas City, KS • +1 (806) 220-3562 • ralucero@me.com
 
PROFESSIONAL PROFILE:
Detail-oriented and solutions-driven information security professional with a strong foundation in regulatory compliance, cybersecurity awareness, and system optimization, seeking to leverage expertise in risk mitigation, secure process design, and cross-functional collaboration to support enterprise-wide security and compliance initiatives within a dynamic organization. Experienced in information security, HR management, and audit compliance, skilled in data management, cybersecurity, risk management, and program development. Proven ability to optimize CRM systems, lead targeted initiatives, and ensure compliance with industry standards.
 
KEY SKILLS:
CRM Software Management | Targeted Student Engagement | Digital Media Content Creation | Public Affairs Strategies | Event Coordination | Cybersecurity Awareness | Program Development | Digital Communication | Budget Management | Community Partnership Development | Financial Management | Educational Program Integration | Financial Literacy Programs | Data Security 
PROFESSIONAL EXPERIENCE:
HRIS Analyst | Unified Government of Wyandotte County, Kansas City, KS                                                          June 2024 – Present
•	System Leadership & Workday Optimization: Led the end-to-end refinement of Workday modules including Absence, HCM, Compensation, Recruiting, and LMS to align functionality with organizational strategy, which improved cross-functional workflows and significantly reduced errors in union-specific payroll processing.
•	Union Leave Plan Administration & Compliance Control: Managed complex structures for 13 bargaining units by configuring accrual logic, entitlement tracking, and separation settlements, which ensured contractual compliance and eliminated discrepancies that previously disrupted payroll accuracy.
•	Cross-Functional Process Integration: Translated multifaceted operational needs into sustainable system solutions by collaborating with business units to implement scalable configurations, which enhanced communication, reduced manual interventions, and improved turnaround time for HR transactions.
•	Compensation Analysis & Learning System Support: Conducted compensation benchmarking and job classification reviews while simultaneously building LMS campaigns and course content, which preserved fair pay practices, maintained FLSA alignment, and boosted employee training participation across departments.
 
Executive Assistant | Boys & Girls Club of America                                                                                                    Dec 2023 – Present
•	Executive Calendar Oversight & Operational Flow: Directed the daily management of the CEO's high-volume schedule by orchestrating meetings, travel logistics, and shifting priorities in real time, which enhanced executive availability, minimized scheduling conflicts, and elevated team-wide productivity.
•	Stakeholder Communication & Relationship Management: Served as the strategic liaison between the executive office and internal/external contacts by managing sensitive correspondence, filtering high-priority inquiries, and providing timely responses, which improved organizational transparency and built long-term trust with partners and community leaders.
•	Executive Event Planning & Strategic Facilitation: Coordinated high-impact board meetings, leadership summits, and donor events by managing logistics, preparing briefing materials, and ensuring alignment with leadership goals, which fostered productive dialogue and led to stronger executive decision-making outcomes.
•	Workflow Optimization & Risk Mitigation: Identified potential roadblocks in administrative and operational processes and implemented preventative solutions before escalation, which safeguarded the continuity of executive initiatives and ensured critical deadlines were consistently met.
 
School Counselor | Amarillo Independent School District | Amarillo, TX                                                            June 2022 - June 2023
•	Student Enrollment Coordination & Family Integration: Led the enrollment intake process by guiding new families through school orientation and providing tailored support services, which significantly reduced administrative congestion and contributed to a 23% drop in first-day office traffic through proactive resource allocation.
•	Group Counseling Facilitation & Emotional Resilience Development: Designed and conducted structured small-group sessions addressing stress and emotional regulation for at-risk students, which led to a 50% self-reported improvement in coping mechanisms and demonstrated measurable impact on overall student mental health.
•	Data-Driven Program Development & Student Engagement: Created targeted counseling initiatives based on performance indicators and behavioral data, which directly resulted in a 70% increase in student participation and improved academic outcomes through early intervention and emotional support.
•	Technical Support & CRM Operations Oversight: Maintained and resolved technical issues within student record systems including Skyward, handling login support, access problems, and data requests, which ensured continuous system usability and strengthened daily instructional support for faculty and staff.
 

Military & College Readiness Coordinator | Amarillo Independent School District | Amarillo, TX                  Aug 2018 - June 2022 
•	CRM Optimization & Program Performance Tracking: Streamlined college and military readiness operations by restructuring CRM data systems to enhance tracking accuracy and student engagement metrics, which led to a 40% increase in program responsiveness and more efficient intervention planning.
•	Strategic Digital Media Production & Student Outreach: Produced and distributed targeted digital content including multimedia campaigns and interactive posts that expanded student awareness of scholarship and enlistment opportunities, resulting in a 30% rise in program engagement across key demographics.
•	Public Engagement Strategy & Community Transparency: Designed and led a metrics-based public outreach initiative leveraging social platforms and school communication tools, which strengthened parent-school relationships and drove a 25% boost in parental involvement in post-secondary planning.
•	Post-Secondary Event Execution & Logistics Oversight: Orchestrated the full lifecycle of college, career, and military preparation events including FAFSA support sessions and recruiter engagements, ensuring smooth coordination, maximized attendance, and tangible readiness outcomes for graduating students.
 
CTE/Business Education Teacher | Amarillo Independent School District | Amarillo, TX                                   Aug 2015 - July 2018
•	Cybersecurity Curriculum Integration & Student Engagement: Embedded cybersecurity concepts into instructional content using interactive digital tools and real-world scenarios, which elevated student participation by 70% and cultivated a more future-ready, tech-aware classroom environment.
•	Program Innovation & Instructional Leadership: Spearheaded the development of forward-thinking educational initiatives that blended cybersecurity principles with instructional design, which modernized existing teaching strategies and introduced cutting-edge learning experiences to diverse student groups.
•	Stakeholder Communication & Digital Information Flow: Facilitated seamless communication across families, staff, and educational partners using secure digital platforms, which enhanced information delivery and reinforced cybersecurity best practices in everyday interactions.
•	Educator Training & Cybersecurity Advocacy: Designed and led tech-centered professional development sessions that equipped faculty with critical cybersecurity knowledge, which promoted a culture of digital responsibility and improved instructional effectiveness across academic departments.
 
EDUCATION:
Master of Education: School Counseling | A&M University
Master of Business Administration: Human Resource Management | Wayland Baptist University
Bachelor of Business Administration: Business Administration | Wayland Baptist University
 
TECHNICAL PROFICIENCY
Security & Compliance: NIST Risk Management Framework (RMF), FISMA, HIPAA, FERPA, Security Awareness Training, Access Control Protocols, Policy Implementation
HRIS Systems: Workday (Absence, HCM, Compensation, LMS, Recruiting), Skyward, FLSA Compliance Tracking, Accrual & Leave Plan Configuration
CRM & Data Management: Salesforce, Microsoft Dynamics, Enrollment & Records Management, CRM Optimization, Data Integrity & Auditing
Learning Management & Educational Tech: Google Classroom, Canvas LMS, Instructional Technology Integration, Cybersecurity Curriculum Development
Communication & Collaboration Tools: Microsoft 365 Suite (Outlook, Excel, Teams, SharePoint), Zoom, Slack, Google Workspace
Digital Content & Event Coordination: Canva, Adobe Express, Social Media Platforms, Event Logistics (FAFSA Nights, Military Recruitments, Career Fairs)
IT & Technical Support: Password Resets, User Account Maintenance, Workflow Troubleshooting, System Access Support
Reporting & Analytics: Ad Hoc Reporting, Metrics Dashboards, Data-Driven Strategy Planning, Internal/External Benchmarking
 
PROJECT MANAGEMENT EXPERIENCE
Workday Absence Redesign (Unified Government of Wyandotte County): Led the reconfiguration of union-specific leave plans and accrual logic across 13 bargaining units, ensuring alignment with labor contracts, improving payroll accuracy, and reducing HR processing errors.
Cybersecurity Awareness Curriculum Implementation (Amarillo ISD): Directed the integration of cybersecurity content into core instruction, managing timelines, instructional design, and stakeholder training, which increased student engagement by 70% and enhanced digital safety practices.
Professional Development Rollout (Amarillo ISD): Coordinated district-wide tech-focused workshops for educators, managing scheduling, communication, and content creation, which resulted in improved cybersecurity literacy and instructional effectiveness.
 

"""

# Mock job data (based on what we extracted earlier)
extracted_data = [
    {
        "location": "San Francisco",
        "job_title": "Data Engineering Manager",
        "apply_link": "https://jobs.ashbyhq.com/openai/b3394315-e8da-4f54-9926-dfe32a1e4913/application",
        "key_skills": [
            "data engineering",
            "leadership",
            "data strategy",
            "data architecture",
            "data quality",
            "data governance",
            "programming languages (Python, Scala, Java)"
        ],
        "compensation": "$405K – $490K • Offers Equity",
        "sub_division_of_organization": "Applied AI"
    },
    {
        "location": "San Francisco",
        "job_title": "Data Engineer, Analytics",
        "apply_link": "https://jobs.ashbyhq.com/openai/fc5bbc77-a30c-4e7a-9acc-8a2e748545b4/application",
        "key_skills": [
            "3+ years of experience as a data engineer",
            "8+ years of software engineering experience",
            "Proficiency in Python, Scala, or Java",
            "Experience with Hadoop, Flink, HDFS, S3",
            "Expertise with ETL schedulers like Airflow, Dagster, Prefect",
            "Solid understanding of Spark"
        ],
        "compensation": "$255K – $405K • Offers Equity",
        "sub_division_of_organization": "Applied AI"
    },
    {
        "location": "San Francisco",
        "job_title": "Backend Software Engineer (Evals)",
        "apply_link": "https://jobs.ashbyhq.com/openai/3d064454-c0c3-4225-bc2c-6d8c0f8735b2/application",
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
        "compensation": "$255K – $405K • Offers Equity",
        "sub_division_of_organization": "Applied AI"
    },
    {
        "location": "San Francisco",
        "job_title": "Backend Software Engineer, Growth",
        "apply_link": "https://jobs.ashbyhq.com/openai/dd2025b9-4d18-4ad7-a78c-7a643419ecc5/application",
        "key_skills": [
            "data analysis",
            "product ideation",
            "experimentation",
            "A/B testing",
            "backend systems",
            "collaboration with cross-functional teams"
        ],
        "compensation": "$160K – $385K • Offers Equity",
        "sub_division_of_organization": "Applied AI"
    },
    {
        "location": "San Francisco",
        "job_title": "Engineering Manager, Data Infrastructure",
        "apply_link": "https://jobs.ashbyhq.com/openai/4f5a0df1-22d7-49a6-8ea1-c15c886fbade/application",
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
        "compensation": "$325K – $405K • Offers Equity",
        "sub_division_of_organization": "Applied AI"
    }
]

def main():
    print(f"{Colors.CYAN}Job Recommendation Agent - Demo Version{Colors.RESET}")
    print(f"{Colors.BLUE}Analyzing {len(extracted_data)} job postings against your resume...{Colors.RESET}")
    
    # Display available jobs
    print(f"\n{Colors.CYAN}Available Jobs:{Colors.RESET}")
    for i, job in enumerate(extracted_data, 1):
        print(f"{Colors.YELLOW}{i}. {job['job_title']} - {job['location']}{Colors.RESET}")
        print(f"   Compensation: {job['compensation']}")
        print(f"   Skills: {', '.join(job['key_skills'][:3])}...")
        print()
    
    # Use OpenAI to analyze and recommend jobs
    prompt = f"""
Please analyze the resume and job listings, and return a JSON list of the top 3 roles that best fit the candidate's experience and skills. Include only the job title, compensation, and apply link for each recommended role. The output should be a valid JSON array of objects in the following format, with no additional text:

[
  {{
    "job_title": "Job Title",
    "compensation": "Compensation (if available, otherwise empty string)",
    "apply_link": "Application URL"
  }},
  ...
]

Based on the following resume:
{resume_paste}

And the following job listings:
{json.dumps(extracted_data, indent=2)}
"""

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response_content = completion.choices[0].message.content.strip()
        # Remove markdown code blocks if present
        if response_content.startswith('```json'):
            response_content = response_content[7:]  # Remove ```json
        if response_content.startswith('```'):
            response_content = response_content[3:]   # Remove ```
        if response_content.endswith('```'):
            response_content = response_content[:-3]  # Remove trailing ```
        
        recommended_jobs = json.loads(response_content.strip())
        
        print(f"{Colors.GREEN}🎯 RECOMMENDED JOBS BASED ON YOUR RESUME:{Colors.RESET}")
        print(f"{Colors.MAGENTA}{'='*60}{Colors.RESET}")
        
        for i, job in enumerate(recommended_jobs, 1):
            print(f"\n{Colors.CYAN}Rank #{i}: {job['job_title']}{Colors.RESET}")
            print(f"{Colors.YELLOW}Compensation: {job['compensation']}{Colors.RESET}")
            print(f"{Colors.BLUE}Apply here: {job['apply_link']}{Colors.RESET}")
            
            # Find the full job details for additional info
            full_job = next((j for j in extracted_data if j['job_title'] == job['job_title']), None)
            if full_job:
                print(f"{Colors.GREEN}Key Skills Match: {', '.join(full_job['key_skills'][:5])}{Colors.RESET}")
        
        print(f"\n{Colors.MAGENTA}{'='*60}{Colors.RESET}")
        print(f"{Colors.GREEN}✨ Analysis complete! These recommendations are based on your experience in:{Colors.RESET}")
        print(f"{Colors.YELLOW}• HRIS/Workday systems management{Colors.RESET}")
        print(f"{Colors.YELLOW}• Data management and CRM optimization{Colors.RESET}")
        print(f"{Colors.YELLOW}• Cybersecurity and compliance{Colors.RESET}")
        print(f"{Colors.YELLOW}• Project management and leadership{Colors.RESET}")
        
    except json.JSONDecodeError as e:
        print(f"{Colors.RED}Error parsing job recommendations JSON: {str(e)}{Colors.RESET}")
        print(f"{Colors.YELLOW}Raw response: {completion.choices[0].message.content[:500]}...{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}Error: {str(e)}{Colors.RESET}")

if __name__ == "__main__":
    main()
