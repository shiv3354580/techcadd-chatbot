from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import markdown
from markdown.extensions.nl2br import Nl2BrExtension


app = Flask(__name__)
CORS(app)

# Initialize OpenAI client
client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1",
)

KNOWLEDGE_BASE = """
============================================================
           TECHCADD COMPUTER EDUCATION - COURSE STRUCTURE
    Best Training Institute in Jalandhar, Punjab (11+ Years Experience)
      ISO 9001:2015 Certified & MSME Registered Institution
============================================================

--- INSTITUTE OVERVIEW ---
TECHCADD is the Best Training Institute in Jalandhar, Punjab with 11+ years of IT training experience.
We offer:
- Practical hands-on training
- Live industry projects
- Regular workshops & seminars
- ISO & MSME certified courses
- 100% placement assistance

--- INSTITUTE CERTIFICATIONS & ACCREDITATIONS ---
TECHCADD Institute is:
1. ISO 9001:2015 CERTIFIED
   - Quality Management System certified
   - International validity
   - Certificate has QR code for scanning and verification
   - Globally recognized standard

2. MSME REGISTERED (Government Registered)
   - Registered under Ministry of Micro, Small & Medium Enterprises
   - Government recognized institution
   - Eligible for government sector benefits
   - Udyam Registration Number available

3. GOVERNMENT APPROVED
   - Recognized by Government authorities
   - Valid for government job applications
   - Accepted in public and private sectors

4. COURSE DELIVERY MODES:
   - Offline Classroom Training
   - Online Live Classes Available
   - Hybrid Mode (Online + Offline)
   - Recorded sessions access
   - 24/7 LMS access

All our certificates include:
✅ QR Code Scanner for verification
✅ ISO 9001:2015 certification mark
✅ MSME registration details
✅ Government registration number
✅ International validity

--- BASIC COMPUTER COURSES ---
Course Name                          Duration      Fees (INR)
------------------------------------------------------------
Punjabi Typing                       1 Month       3,500
- What you will learn: Punjabi keyboard layout (AnmolLipi / Raavi), Typing accuracy & speed improvement, Office & government typing formats
- Projects: Typing official letters in Punjabi, Paragraph & document typing, Speed test certification task

Advanced Excel                       1 Month       4,500
- What you will learn: Advanced formulas & functions, Pivot tables & dashboards, Data analysis & reports
- Projects: Sales data analysis dashboard, Employee attendance tracker, Business expense management system

Basic Computer                       2 Months      6,500
- What you will learn: Computer fundamentals, MS Word, Excel & PowerPoint, Internet & email handling
- Projects: Resume & office letter creation, Monthly expense Excel sheet, Business presentation project

Quickbooks                           45 Days       10,500
- What you will learn: Accounting basics, GST & payroll, Financial reporting
- Projects: Company accounting setup, GST return preparation, Profit & loss report generation

Tally ERP-9                          2 Months      11,500
- What you will learn: Accounting & taxation, Inventory & payroll, GST reports
- Projects: Complete company accounts, Inventory & GST billing system, Final balance sheet preparation

Diploma in Computer Application      1 Year        36,500
- What you will learn: Office automation, Accounting basics, Programming fundamentals
- Projects: Office management system, Computerized billing system, Mini software project

--- CIVIL ENGINEERING COURSES ---
Course Name                          Duration      Fees (INR)
------------------------------------------------------------
Basic Autocad                        45 Days       9,500
- Projects: 2D house plan, Office layout drawing, Structural detailing drawing

Advanced Autocad                     2 Months      12,500
- Projects: Complete residential building drawing set, Commercial floor plan, Construction working drawings

Prima Veera                          1 Month       12,500
- Projects: Construction project scheduling, Resource & cost planning, Project progress report

MSP                                  1 Month       12,500
- Projects: Project timeline creation, Resource allocation project, Gantt chart-based project report

Revit                                2 Months      14,500
- Projects: 3D residential building model, BIM-based construction drawings, Quantity takeoff project

Sketchup + V RAY                     2 Months      14,500
- Projects: Interior design visualization, Exterior 3D walkthrough, Photorealistic rendering project

Staad Pro                            1 Month       15,500
- Projects: RCC building structural analysis, Load calculation project, Structural safety report

E Tab                                1 Month       15,500
- Projects: Multi-storey building analysis, Earthquake load analysis, Structural design report

3DX Max                              2 Months      16,500
- Projects: Architectural visualization project, Product animation project, Interior rendering project

Revit-Enscape                        4 Months      18,500
- Projects: Real-time 3D walkthrough, VR-enabled building visualization, Client presentation project

3DX Max + V RAY + Photoshop          4 Months      22,500
- Projects: Architectural visualization with rendering and post-processing

Diploma In Civil CADD                3 Months      26,500
- Projects: Complete building project (start to finish), Architectural + structural drawings, Real site-based civil project

Professional Diploma in Civil CADD   4 Months      34,500
- Projects: Advanced civil engineering projects, Commercial building design, Structural analysis projects

Master Diploma in Civil CADD         6 Months      42,500
- Projects: Comprehensive civil engineering projects, Highway design, Bridge design, Advanced structural projects

--- MECHANICAL ENGINEERING COURSES ---
Course Name                          Duration      Fees (INR)
------------------------------------------------------------
Work NC                              1 Month       18,500
- Projects: CNC machining simulation, Toolpath optimization project, Manufacturing process project

Autocad                              45 Days       18,500
- Projects: Machine component drawing, Assembly drawing project, Manufacturing blueprint

Catia                                3 Months      18,500
- Projects: Mechanical part design, Product assembly design, Surface modeling project

NX Cad + NX Cam                      3 Months      18,500
- Projects: CAD modeling project, CAM toolpath programming, CNC machining simulation

Diploma in Mechanical CADD           3 Months      18,500
- Projects: Industrial product design, Manufacturing workflow project, Live mechanical industry project

Master Diploma in Mechanical CADD    6 Months      18,500
- Projects: Advanced mechanical engineering projects, Automotive design, Aerospace components design

--- PROGRAMMING & WEB DEVELOPMENT ---
Course Name                          Duration      Fees (INR)
------------------------------------------------------------
Core Python                          2 Months      12,500
- What you will learn: Python fundamentals, syntax, functions, loops, file handling, OOPs concepts
- Projects: Student management system, File handling mini project, Automation script project

C / C++                              2 Months      15,500
- What you will learn: C basics, C++ OOPs, Data structures, Algorithms
- Projects: Banking management system, Library management system, Console-based applications

Java                                 2 Months      15,500
- What you will learn: Java fundamentals, OOPs, JDBC, Swing
- Projects: Desktop application, JDBC database project, Multithreaded application

Web Designing (Basic)                2 Months      15,500
- What you will learn: HTML5, CSS3, JavaScript, Bootstrap
- Projects: Personal portfolio website, Business website, Responsive landing page

Web Development (PHP/MySQL)          4 Months      25,500
- What you will learn: PHP, MySQL, JavaScript, AJAX
- Projects: Dynamic website, Login & authentication system, CRUD-based web application

Web Development (Python/Django)      4 Months      28,500
- What you will learn: Django framework, Python web development, Database integration
- Projects: Django web application, E-commerce site, Blog application

Drop Shipping                        3 Months      30,500
- What you will learn: E-commerce basics, Product sourcing, Order fulfillment, Marketing
- Projects: E-commerce store setup, Product listing creation, Order management system

PHP (Frontend + Backend)             6 Months      36,500
- What you will learn: Full-stack PHP development, Laravel framework, API development
- Projects: Full-stack PHP application, Inventory management system, E-commerce platform

Python + Machine Learning            4 Months      38,500
- What you will learn: Python for ML, Scikit-learn, TensorFlow basics, Data preprocessing
- Projects: Spam detection system, Sales prediction model, Data analysis project

Python (Frontend + Backend)          6 Months      42,500
- What you will learn: Django/Flask, React.js, REST APIs, Database design
- Projects: Full-stack Python application, Social media app, Real-time chat application

MERN Stack                           6 Months      42,500
- What you will learn: MongoDB, Express.js, React.js, Node.js
- Projects: Full-stack web application, REST API project, Real-time web app

Full Stack in PHP (Laravel)          6 Months      42,500
- What you will learn: Laravel framework, Vue.js/React, API development, Deployment
- Projects: Laravel web application, CRM system, Job portal

Digital Marketing                    6 Months      45,500
- What you will learn: SEO, SEM, Social Media Marketing, Email Marketing, Analytics
- Projects: Live SEO optimization project, Google Ads campaign, Social media marketing campaign

Cyber Security                       6 Months      50,500
- What you will learn: Ethical hacking, Network security, Cryptography, Penetration testing
- Projects: Website vulnerability testing, Ethical hacking lab project, Network security analysis

--- PROFESSIONAL CERTIFICATIONS ---
Course Name                          Duration      Fees (INR)
------------------------------------------------------------
Industrial Training                  6 Months      36,500
- Projects: Industry-based live project, Internship project report, Final practical assessment

Professional Cert. (Web Design)      6 Months      40,500
- Projects: Professional web design projects, Client websites portfolio

Advanced Cert. in AI & Data Science  6 Months      (Contact)
- What you will learn: AI concepts, Data science, Machine learning algorithms, Deep learning
- Projects: Machine learning prediction system, Data visualization dashboard, AI-based real-world project
- Fees: Contact the institute for pricing details

Cloud Computing & DevOps             6 Months      (Contact)
- What you will learn: AWS/Azure, Docker, Kubernetes, CI/CD pipelines
- Projects: Cloud infrastructure setup, CI/CD pipeline implementation, Application deployment project
- Fees: Contact the institute for pricing details

Financial Modeling & Accounting      6 Months      (Contact)
- What you will learn: Financial analysis, Accounting software, Tax planning, Audit
- Projects: Financial modeling projects, Tax computation, Audit report preparation
- Fees: Contact the institute for pricing details

--- ADMISSIONS & ENROLLMENT ---
ADMISSION PROCESS:
1. Visit institute or apply online through website
2. Free career counseling session
3. Course selection guidance
4. Submit required documents
5. Course fee payment
6. Batch allocation and commencement

REQUIRED DOCUMENTS:
- 10th/12th Marksheet (photocopy)
- Graduation marksheet (if applicable)
- Aadhar Card copy (2 copies)
- Passport size photos (4)
- Address proof
- Transfer certificate (if required)

PAYMENT OPTIONS:
- Cash Payment
- Credit/Debit Card
- UPI (GPay, PhonePe, Paytm)
- Bank Transfer/Net Banking
- Cheque (subject to clearance)
- Installment facility available

BATCH TIMINGS:
- Morning Batch: 9:00 AM - 12:00 PM
- Afternoon Batch: 2:00 PM - 5:00 PM
- Evening Batch: 6:00 PM - 9:00 PM
- Weekend Batches: Saturday & Sunday (10 AM - 4 PM)
- Fast Track Batches: Available on request

INSTALLMENT FACILITY:
- Available for courses above ₹20,000
- 50% payment at admission
- 25% after 1 month
- 25% after 2 months
- Zero interest charges
- Flexible plans available

DISCOUNTS AVAILABLE:
- Early Bird Discount (10%)
- Group Enrollment Discount (15% for 3+ students)
- Referral Discount (10%)
- Scholarship for meritorious students
- Special discounts for women candidates

--- PLACEMENT & CAREER SUPPORT ---
PLACEMENT ASSISTANCE:
- 100% Placement Assistance
- Resume preparation workshop
- Interview preparation sessions
- Mock interviews
- Soft skills training
- Job placement support
- Regular placement drives

COMPANIES WE PLACE IN:
- IT Companies (TCS, Infosys, Wipro, Tech Mahindra)
- Construction Firms
- Manufacturing Industries
- Web Development Agencies
- CAD/CAM Companies
- Government Projects
- E-commerce Companies
- Digital Marketing Agencies

INTERNSHIP OPPORTUNITIES:
- 3-6 months paid/unpaid internship
- Live project work with companies
- Industry exposure
- Certificate of internship
- Stipend based on performance
- Convert to full-time job opportunities

CAREER GUIDANCE:
- Free career counseling
- Course selection help based on aptitude
- Skill gap analysis
- Future scope guidance
- Higher education guidance
- Entrepreneurship support

PLACEMENT RECORD:
- 90% placement rate
- Average starting salary: ₹2.5 - ₹4.5 LPA
- Highest package: ₹8.5 LPA
- 200+ companies in placement network
- Regular campus drives

--- FACILITIES & INFRASTRUCTURE ---
CLASSROOM FACILITIES:
- Air-conditioned computer labs
- High-speed computers (i5/i7 processors)
- Latest software installed
- LCD projectors & smart boards
- Library with technical books
- Wi-Fi campus
- Power backup (UPS/Generator)

LAB FACILITIES:
- Computer Labs: 100+ systems
- Civil CADD Lab with latest software
- Mechanical CADD Lab
- Programming Lab
- Networking Lab
- Hardware Lab
- Project Lab

ADDITIONAL SUPPORT:
- Free study material (printed)
- eBooks & video tutorials
- 24/7 practice lab access
- Doubt clearing sessions
- Project guidance
- One-on-one mentoring
- Alumni network access

WORKSHOPS & EVENTS:
- Regular technical workshops
- Guest lectures from industry experts
- Hackathons and coding competitions
- Project exhibitions
- Career fairs
- Seminar on latest technologies

LIBRARY FACILITIES:
- Technical books collection
- Reference books
- Magazines and journals
- Previous project reports
- Online journal access
- Reading room

--- CERTIFICATION DETAILS ---
CERTIFICATE TYPES:
1. Course Completion Certificate (TECHCADD)
2. ISO 9001:2015 Certified Certificate
3. MSME Registered Certificate
4. Government Recognized Certificate
5. International Validity Certificate
6. Internship Certificate
7. Project Completion Certificate

CERTIFICATE FEATURES:
- Bilingual (English & Hindi)
- QR Code for online verification
- Security hologram
- Unique serial number
- Institute seal and signature
- Online verification portal access
- Digital certificate available

VERIFICATION PROCESS:
1. Scan QR code on certificate using smartphone
2. Visit verification portal: verify.techcadd.com
3. Enter certificate serial number
4. Verify authenticity and details online
5. Download digital copy if needed
6. Print certificate if required

CERTIFICATE VALIDITY:
- Lifetime validity
- Internationally recognized
- Accepted by government and private sectors
- Valid for higher education
- Valid for jobs in India and abroad
- Can be verified anytime online

--- CONTACT & LOCATION ---
HEAD OFFICE:
TECHCADD Computer Education Pvt. Ltd.
2nd Floor, Crystal Plaza, SCS 78
Opposite PIMS Hospital
Jalandhar, Punjab 144001
India

CONTACT DETAILS:
Phone: +91 9888122255 (Call/WhatsApp)
Landline: 0181-5071111
Email: info@techcadd.com
Website: www.techcadd.com
WhatsApp: https://wa.me/919888122255

BRANCHES:
1. JALANDHAR-1: opp. All India Radio Station, near Bus Stand, New Jawahar Nagar, Jawahar Nagar, Jalandhar, Punjab 144001
2. JALANDHAR-2: 2nd floor, Crystal Plaza, SCS 78, opp. Pims Hospital, Jalandhar, Punjab 144001
3. PHAGWARA: 1st Floor, Chadha Business Park, Bus Stand, Grand Trunk Rd, near ICIC Bank, opp. Lovely Bajaj Autos, Sondhi Chowk, Phagwara, Punjab 144401
4. CHANDIGARH: Plot number F-547 3rd floor Industrial Area, 8A, Sector 75, Sahibzada Ajit Singh Nagar, Punjab 160055
5. MAQSUDAN: Computer Center First Floor Vidya Square Buliding Near Maqsudan Flyover, Chowk, Maqsudan, Jalandhar, Punjab 144027
6. HOSHIARPUR:  Near, SCO 29 A Ground Floor City Center, Bus Stand Rd, Hoshiarpur, Punjab 146001
7. LUDHIANA: 1st Floor, Sear Complex, 773/1, Bharat Nagar, chowk, Ludhiana 

SOCIAL MEDIA:
Facebook: https://www.facebook.com/techcaddcomputereducationjalandhar/
Instagram: https://www.instagram.com/techcadd__jalandhar/
LinkedIn: https://in.linkedin.com/company/techcadd-computer-education-pvt-ltd
YouTube: https://www.youtube.com/channel/UCh-cEDwb1MA6W0hoX0qoDog
Twitter/X: https://x.com/Techcadd_comp
WhatsApp: https://wa.me/919888122255

OFFICE HOURS:
Monday - Saturday: 9:00 AM - 7:00 PM
Sunday: 10:00 AM - 4:00 PM
24/7 Online Support Available

GOOGLE MAPS:
Head Office Location: https://www.google.com/maps/place/TechCADD/@31.3156448,75.5847976,17z/data=!3m1!4b1!4m6!3m5!1s0x391a5b91e848f031:0xa93511a827bfa41f!8m2!3d31.3156402!4d75.5873725!16s%2Fg%2F11g0klygx5?entry=ttu&g_ep=EgoyMDI2MDEyNS4wIKXMDSoASAFQAw%3D%3D

--- FREQUENTLY ASKED QUESTIONS ---
Q: Is there any discount available?
A: Yes, we offer:
   - Early bird registration discount (10%)
   - Group enrollment discount (15% for 3+ students)
   - Scholarship for meritorious students
   - Referral discounts (10%)
   - Special discounts for women candidates

Q: Can I get a demo class?
A: Yes, free demo classes available:
   - Every Saturday (10 AM - 12 PM)
   - Book in advance through phone/website
   - Experience teaching methodology
   - Meet faculty members
   - See infrastructure

Q: What if I miss classes?
A: We provide:
   - Recorded session access
   - Extra classes on weekends
   - Doubt clearing sessions
   - Batch change option
   - One-on-one support

Q: Is hostel facility available?
A: We provide assistance with:
   - PG accommodations near institute
   - Hostel references
   - Safe and affordable options
   - Food facilities information

Q: Is the course available in Hindi?
A: Yes, teaching available in:
   - Hindi medium
   - English medium
   - Mixed mode as per student preference
   - Bilingual study material

Q: Can I pay fees in installments?
A: Yes, installment facility:
   - Available for courses above ₹20,000
   - 50% at admission, 25% after 1 month, 25% after 2 months
   - Zero interest charges
   - Flexible payment plans

Q: Do you provide study material?
A: Yes, we provide:
   - Printed notes and books
   - eBooks and PDFs
   - Video tutorials
   - Practice assignments
   - Project files and templates
   - Software installation help

Q: Is there any age limit?
A: Minimum age: 16 years
   No maximum age limit
   Special batches for working professionals

Q: What are the eligibility criteria?
A: Basic criteria:
   - 10th pass for basic computer courses
   - 12th pass for diploma courses
   - Graduation for professional courses
   - Basic computer knowledge preferred
   (Specific requirements may vary by course)

Q: Do you provide job guarantee?
A: We provide:
   - 100% placement assistance
   - Regular placement drives
   - Interview preparation
   - Resume building
   - Not a 100% job guarantee, but excellent placement record

Q: Are courses available online?
A: Yes, we offer:
   - Live online classes
   - Recorded sessions
   - Online doubt clearing
   - Virtual lab access
   - Online exams and certification

Q: How do I verify certificate?
A: Certificate verification:
   - Scan QR code on certificate
   - Visit verify.techcadd.com
   - Enter certificate number
   - Verify online 24/7

--- COURSE RECOMMENDATIONS ---
BASED ON EDUCATIONAL BACKGROUND:

For 10th/12th Pass Students:
- Basic Computer Course
- Tally ERP-9
- Web Designing
- AutoCAD Basic
- Digital Marketing

For Graduates (Any Stream):
- Web Development
- Python Programming
- Digital Marketing
- CAD/CAM Courses
- Data Science basics

For Engineering Graduates:
- Advanced CADD courses
- Programming courses
- Data Science & AI
- Cloud Computing
- Cyber Security

For Working Professionals:
- Advanced Excel
- Digital Marketing
- Python for automation
- QuickBooks/Tally
- Project Management tools

BASED ON CAREER GOALS:

For Government Jobs:
- Basic Computer Course
- Tally ERP-9
- Advanced Excel
- Punjabi Typing
- DCA (Diploma in Computer Application)

For Private Sector Jobs:
- Web Development
- Python Programming
- Digital Marketing
- CAD/CAM Courses
- Data Science

For Higher Studies Abroad:
- Advanced Programming
- Data Science & AI
- Cloud Computing
- Cyber Security
- Professional Certifications

For Entrepreneurs/Business:
- Digital Marketing
- QuickBooks/Tally
- Web Development
- E-commerce/Drop Shipping
- Financial Modeling

POPULAR COURSE COMBINATIONS:
1. Web Designing + Digital Marketing (6 months)
2. Python + Machine Learning (6 months)
3. AutoCAD + Revit (4 months)
4. Tally + Advanced Excel (3 months)
5. Basic Computer + DCA (1 year)

HIGH DEMAND COURSES 2024:
1. Python + Machine Learning
2. MERN Stack Development
3. Digital Marketing
4. Cyber Security
5. Data Science & AI
6. Cloud Computing
7. AutoCAD & Revit
8. Tally with GST

SHORT-TERM CERTIFICATIONS (1-3 months):
- Advanced Excel
- Tally ERP-9
- Web Designing
- AutoCAD Basic
- Digital Marketing Basics
- Python Basics

LONG-TERM DIPLOMAS (6-12 months):
- Full Stack Development
- Data Science & AI
- Cyber Security
- Civil CADD Master Diploma
- Mechanical CADD Master Diploma
- Digital Marketing Professional

============================================================
Note: All fees are subject to change. Please contact institute for latest fee structure.
Weekend batches and online classes available for all courses.
ISO 9001:2015 Certified | MSME Registered | Government Approved
============================================================
"""

SYSTEM_PROMPT = """
You are TECHCADD, an AI admission counselor for TECHCADD Computer Education Institute.
You are friendly, professional, and helpful.

USE THIS KNOWLEDGE BASE:
{knowledge_base}

RESPONSE GUIDELINES:
1. ALWAYS mention: "ISO 9001:2015 Certified, MSME Registered, Government Approved Institute"
2. For course queries: Provide duration, fees, what you learn, projects
3. For admissions: Explain process, documents, payment options, batch timings
4. For certification: Mention QR code scanning, online verification, international validity
5. For placement: Mention 100% assistance, companies, internship opportunities
6. For contact: Provide address: "2nd Floor, Crystal Plaza, SCS 78, opp. Pims Hospital, Jalandhar"
   Phone: "+91 9888122255", Email: "info@techcadd.com"
7. For branches: List all 7 branches
8. For comparisons: Suggest based on educational background and career goals
9. For facilities: Mention AC labs, latest computers, 24/7 lab access
10. For online classes: Mention live online classes, recorded sessions, hybrid mode

BE SPECIFIC WITH DETAILS:
- Always mention exact durations and fees when available
- Mention "Contact for pricing" if fees show (Contact)
- Provide social media links when relevant
- Mention installment options for courses above ₹20,000
- Always end with contact encouragement

If unsure: Ask clarifying questions or suggest calling +91 9888122255 for immediate assistance.
"""

# Store chat history per session
chat_histories = {}

def get_chat_response(user_message, session_id='default'):
    if session_id not in chat_histories:
        chat_histories[session_id] = []
    
    # Build the prompt with knowledge base
    system_content = SYSTEM_PROMPT.format(knowledge_base=KNOWLEDGE_BASE)
    
    messages = [
        {"role": "system", "content": system_content},
    ]
    
    # Add previous messages from this session
    messages.extend(chat_histories[session_id])
    
    # Add new user message
    messages.append({"role": "user", "content": user_message})
    
    try:
        response = client.responses.create(
            model="openai/gpt-oss-20b",
            input=messages,
        )
        
        assistant_reply = response.output_text
        
        # Save conversation
        chat_histories[session_id].append({"role": "user", "content": user_message})
        chat_histories[session_id].append({"role": "assistant", "content": assistant_reply})
        
        # Keep only last 10 messages to prevent context overflow
        if len(chat_histories[session_id]) > 10:
            chat_histories[session_id] = chat_histories[session_id][-10:]
        
        return assistant_reply
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    session_id = data.get('session_id', 'default')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    markdown_response = get_chat_response(user_message, session_id)
    
    # Convert Markdown to HTML automatically
    html_response = markdown.markdown(
        markdown_response,
        extensions=[
            'nl2br',        # Convert newlines to <br>
            'sane_lists',   # Better list handling
            'fenced_code'   # Support for code blocks
        ]
    )
    return jsonify({
        'response': html_response,
        'session_id': session_id
    })
   

@app.route('/clear', methods=['POST'])
def clear_chat():
    data = request.json
    session_id = data.get('session_id', 'default')
    
    if session_id in chat_histories:
        chat_histories[session_id] = []
    
    return jsonify({'success': True, 'message': 'Chat history cleared'})
@app.route('/widget')
def widget():
    """Serve the chat widget as a standalone page"""
    return render_template('widget.html')

@app.route('/widget-embed')
def widget_embed():
    """Widget embed code for other websites"""
    return '''
    <!-- TechCADD Chat Widget -->
    <div id="techcadd-chat-widget"></div>
    <script>
        (function() {
            var d = document, s = d.createElement('script');
            s.src = 'https://chatbott.techcadd.com//static/widget.js';  // Your widget JS
            s.async = true;
            d.getElementsByTagName('head')[0].appendChild(s);
        })();
    </script>
    '''
if __name__ == '__main__':

    app.run(debug=True, port=5000)
