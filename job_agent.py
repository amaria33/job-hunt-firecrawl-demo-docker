# %%
# %%
import os
import requests
import json
from dotenv import load_dotenv
from openai import OpenAI

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

# Initialize the FirecrawlApp with your API key
firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set the jobs page URL - using a more accessible jobs site
jobs_page_url = "https://jobs.ashbyhq.com/openai","https://openai.com/careers/search"

# Resume
resume_paste = """"
R. Ashley Maria, MBA, M.Ed.
Kansas City, KS • +1 (806) 220-3562 • ralucero@me.com
 
PROFESSIONAL PROFILE:
Detail-oriented and solutions-driven human resources professional with a strong foundation in regulatory compliance, cybersecurity awareness, and system optimization, seeking to leverage expertise in risk mitigation, secure process design, and cross-functional collaboration to support enterprise-wide security and compliance initiatives within a dynamic organization. Experienced in information security, HR management, and audit compliance, skilled in data management, cybersecurity, risk management, and program development. Proven ability to optimize CRM systems, lead targeted initiatives, and ensure compliance with industry standards.
 
KEY SKILLS:
CRM Software Management | Targeted Student Engagement | Digital Media Content Creation | Public Affairs Strategies | Event Coordination | Cybersecurity Awareness | Program Development | Digital Communication | Budget Management | Community Partnership Development | Financial Management | Educational Program Integration | Financial Literacy Programs | Data Security 
PROFESSIONAL EXPERIENCE:
HRIS Analyst | Unified Government of Wyandotte County, Kansas City, KS                                                          June 2024 – Present
•	System Leadership & Workday Optimization: Led the end-to-end refinement of Workday modules including Absence, HCM, Compensation, Recruiting, and LMS to align functionality with organizational strategy, which improved cross-functional workflows and significantly reduced errors in union-specific payroll processing.
•	Union Leave Plan Administration & Compliance Control: Managed complex structures for 13 bargaining units by configuring accrual logic, entitlement tracking, and separation settlements, which ensured contractual compliance and eliminated discrepancies that previously disrupted payroll accuracy.
•	Cross-Functional Process Integration: Translated multifaceted operational needs into sustainable system solutions by collaborating with business units to implement scalable configurations, which enhanced communication, reduced manual interventions, and improved turnaround time for HR transactions.
•	Compensation Analysis & Learning System Support: Conducted compensation benchmarking and job classification reviews while simultaneously building LMS campaigns and course content, which preserved fair pay practices, maintained FLSA alignment, and boosted employee training participation across departments.
 
Executive Assistant | Boys & Girls Club of America                                                                                                    Dec 2023 – Present
•	Executive Calendar Oversight & Operational Flow: Directed the daily management of the CEO’s high-volume schedule by orchestrating meetings, travel logistics, and shifting priorities in real time, which enhanced executive availability, minimized scheduling conflicts, and elevated team-wide productivity.
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

# First, scrape the jobs page using Firecrawl
try:
    response = requests.post(
        "https://api.firecrawl.dev/v1/scrape",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {firecrawl_api_key}"
        },
        json={
            "url": jobs_page_url,
            "formats": ["markdown"],
            "waitFor": 2000,
            "timeout": 30000
        }
    )
    
    if response.status_code == 200:
        result = response.json()
        if result.get('success'):
            html_content = result['data']['markdown']
            # Define the O1 prompt for extracting apply links
            prompt = f"""
            Extract up to 3 job application links from the given markdown content.
            Return the result as a JSON object with a single key 'apply_links' containing an array of strings (the links).
            The output should be a valid JSON object, with no additional text.
            Do not include any JSON markdown formatting or code block indicators.
            Provide only the raw JSON object as the response.

            Example of the expected format:
            {{"apply_links": ["https://example.com/job1", "https://example.com/job2", ...]}}

            Markdown content:
            {html_content[:50000]}
            """
            print(f"{Colors.GREEN}Successfully scraped the jobs page{Colors.RESET}")
        else:
            print(f"{Colors.RED}Failed to scrape the jobs page: {result.get('message', 'Unknown error')}{Colors.RESET}")
            html_content = ""
    else:
        print(f"{Colors.RED}Error {response.status_code}: {response.text}{Colors.RESET}")
        html_content = ""
except requests.RequestException as e:
    print(f"{Colors.RED}An error occurred while scraping: {str(e)}{Colors.RESET}")
    html_content = ""
except json.JSONDecodeError as e:
    print(f"{Colors.RED}Error decoding JSON response: {str(e)}{Colors.RESET}")
    html_content = ""
except Exception as e:
    print(f"{Colors.RED}An unexpected error occurred while scraping: {str(e)}{Colors.RESET}")
    html_content = ""

# Extract apply links from the scraped HTML using O1
apply_links = []
if html_content:
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
        
        if completion.choices:
            response_content = completion.choices[0].message.content.strip()
            print(f"{Colors.BLUE}Raw response length: {len(response_content)} characters{Colors.RESET}")
            
            try:
                result = json.loads(response_content)
                apply_links = result['apply_links']
                print(f"{Colors.GREEN}Successfully extracted {len(apply_links)} apply links{Colors.RESET}")
            except json.JSONDecodeError as e:
                print(f"{Colors.RED}Error parsing apply links JSON: {str(e)}{Colors.RESET}")
                print(f"{Colors.YELLOW}Raw response (first 500 chars): {response_content[:500]}...{Colors.RESET}")
                apply_links = []
        else:
            print(f"{Colors.RED}No apply links extracted{Colors.RESET}")
            apply_links = []
    except json.JSONDecodeError as e:
        print(f"{Colors.RED}Error decoding JSON from OpenAI response: {str(e)}{Colors.RESET}")
    except KeyError as e:
        print(f"{Colors.RED}Expected key not found in OpenAI response: {str(e)}{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}An unexpected error occurred during extraction: {str(e)}{Colors.RESET}")
else:
    print(f"{Colors.RED}No HTML content to process{Colors.RESET}")

# Initialize a list to store the extracted data
extracted_data = []


# %%
print(f"{Colors.CYAN}Apply links:{Colors.RESET}")
for link in apply_links:
    print(f"{Colors.YELLOW}{link}{Colors.RESET}")

# %%
# Process each apply link
for index, link in enumerate(apply_links):
    try:
        response = requests.post(
            "https://api.firecrawl.dev/v1/scrape",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {firecrawl_api_key}"
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
                extracted_data.append(result['data']['extract'])
                print(f"{Colors.GREEN}Data extracted for job {index + 1}/{len(apply_links)}{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}Failed to extract data for job {index + 1}: {result.get('message', 'Unknown error')}{Colors.RESET}")
        else:
            print(f"{Colors.RED}Error {response.status_code} for job {index + 1}: {response.text[:100]}...{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}Exception for job {index + 1}: {str(e)[:100]}...{Colors.RESET}")


# %%
# %%
# Print the extracted data
print(f"{Colors.CYAN}Extracted data:{Colors.RESET}")
for job in extracted_data:
    print(json.dumps(job, indent=2))
    print(f"{Colors.MAGENTA}{'-' * 50}{Colors.RESET}")


# %%




# Use o1-preview to choose which jobs should be applied to based on the resume
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

if extracted_data:
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
            response_content = response_content[7:]  # Remove ```json
        if response_content.startswith('```'):
            response_content = response_content[3:]   # Remove ```
        if response_content.endswith('```'):
            response_content = response_content[:-3]  # Remove trailing ```
        
        recommended_jobs = json.loads(response_content.strip())
        print(f"{Colors.CYAN}Recommended jobs:{Colors.RESET}")
        print(json.dumps(recommended_jobs, indent=2))
    except json.JSONDecodeError as e:
        print(f"{Colors.RED}Error parsing job recommendations JSON: {str(e)}{Colors.RESET}")
        print(f"{Colors.YELLOW}Raw response: {completion.choices[0].message.content[:500]}...{Colors.RESET}")
else:
    print(f"{Colors.RED}No job data extracted, cannot generate recommendations{Colors.RESET}")

