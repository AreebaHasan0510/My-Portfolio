"""
Portfolio Data Store for Areeba Hasan - Data Analyst & Data Scientist
"""

PROFILE_DATA = {
    "name": "Areeba Hasan",
    "title": "Data Analyst | Data Scientist",
    "email": "areebhas0510@gmail.com",
    "phone": "+91-9628250000",
    "location": "Lucknow, UP, India",
    "github": "https://github.com/AreebaHasan0510",
    "linkedin": "https://www.linkedin.com/in/areeba-hasan-4731b9318",
    "portfolio": "http://localhost:8000",
    "status": "Available for Data Science & Analyst Roles",
    "summary": (
        "Enthusiastic final-year Computer Science student specializing in Data Science, "
        "with hands-on experience in Python, Machine Learning, AI Data Analytics, and backend development. "
        "Skilled in building data-driven applications using FastAPI, MySQL, MongoDB, Power BI, "
        "and modern web technologies. Experienced in developing real-world projects, including an Advanced "
        "Credit Card Fraud Detection system integrating machine learning, authentication, dashboard visualization, "
        "and database connectivity. Strong problem-solving abilities with a passion for leveraging AI, data, "
        "and technology to build practical and intelligent solutions."
    ),
    "stats": [
        {"label": "Years Experience", "value": "1+", "suffix": "Yrs"},
        {"label": "ML & Analytics Projects", "value": "5+", "suffix": "Projects"},
        {"label": "Profit Margin Boosted", "value": "15%", "suffix": "Uplift"},
        {"label": "Hackathons & Awards", "value": "3+", "suffix": "Badges"}
    ]
}

SKILLS_DATA = [
    {
        "category": "Languages",
        "icon": "code",
        "skills": [
            {"name": "Python", "level": 95, "tag": "Primary"},
            {"name": "SQL", "level": 90, "tag": "Database"},
            {"name": "JavaScript", "level": 85, "tag": "Web"},
            {"name": "TypeScript", "level": 80, "tag": "Frontend"}
        ]
    },
    {
        "category": "Frameworks & APIs",
        "icon": "cpu",
        "skills": [
            {"name": "FastAPI", "level": 92, "tag": "Backend"},
            {"name": "Vector DBs (Chroma DB)", "level": 88, "tag": "AI/RAG"},
            {"name": "Node.js & Express.js", "level": 82, "tag": "Backend"}
        ]
    },
    {
        "category": "Machine Learning & NLP",
        "icon": "brain",
        "skills": [
            {"name": "Scikit-learn", "level": 90, "tag": "ML Core"},
            {"name": "Classification & Regression", "level": 92, "tag": "Modeling"},
            {"name": "Feature Engineering", "level": 88, "tag": "Data Prep"},
            {"name": "Sentence Transformers & NLP", "level": 85, "tag": "AI/LLM"}
        ]
    },
    {
        "category": "Data Analytics & BI",
        "icon": "bar-chart-2",
        "skills": [
            {"name": "Power BI", "level": 94, "tag": "BI Dashboards"},
            {"name": "Tableau", "level": 88, "tag": "Visualization"},
            {"name": "Pandas & NumPy", "level": 95, "tag": "Data Manipulation"},
            {"name": "KPI Analytics & Insights", "level": 90, "tag": "Business"}
        ]
    },
    {
        "category": "Databases & Tools",
        "icon": "database",
        "skills": [
            {"name": "MySQL", "level": 90, "tag": "RDBMS"},
            {"name": "MongoDB", "level": 84, "tag": "NoSQL"},
            {"name": "Git & GitHub", "level": 92, "tag": "DevOps"},
            {"name": "REST APIs", "level": 94, "tag": "Integration"}
        ]
    }
]

EXPERIENCE_DATA = [
    {
        "role": "Python Developer Intern",
        "company": "Client Code AI Innovation Pvt. Ltd",
        "location": "Faridabad, India · Remote",
        "period": "June 2026 – July 2026",
        "type": "Internship",
        "highlights": [
            "Developed and implemented Python-based applications focusing on writing clean, efficient, and maintainable code.",
            "Applied advanced Python programming concepts to solve complex real-world software & automation tasks.",
            "Collaborated with cross-functional teams to debug, refactor, and optimize backend server performance."
        ],
        "technologies": ["Python", "FastAPI", "REST APIs", "Debugging", "Git"]
    },
    {
        "role": "AI & Data Analytics Intern",
        "company": "In Amigos Foundation",
        "location": "Virtual",
        "period": "June 2026 – July 2026",
        "type": "Internship",
        "highlights": [
            "Analyzed multi-dimensional datasets to extract actionable insights and trends supporting executive decision-making.",
            "Engineered AI-powered analytical models to automate data processing and pattern detection.",
            "Designed visualizations and executive summaries highlighting business key performance indicators (KPIs)."
        ],
        "technologies": ["Python", "Pandas", "AI Analytics", "Data Visualization", "SQL"]
    }
]

PROJECTS_DATA = [
    {
        "id": "credit-card-fraud",
        "title": "Credit Card Fraud Detection System",
        "category": "Machine Learning & Security",
        "subtitle": "Real-time ML Fraud Risk Prediction & MySQL Dashboard",
        "period": "2026",
        "technologies": ["HTML", "FastAPI", "Machine Learning", "MySQL", "Python", "Scikit-Learn"],
        "summary": "An enterprise-grade fraud detection system leveraging Scikit-learn classification models, FastAPI REST endpoints, and live risk analytics to protect transaction pipelines.",
        "points": [
            "Integrated trained ML classification models to identify fraudulent financial transactions with ultra-high precision.",
            "Built interactive web application using FastAPI with secure authentication, real-time prediction engine, and interactive dashboard.",
            "Connected system to MySQL database for transaction persistence, audit logging, and risk analytics."
        ],
        "has_demo": True,
        "demo_type": "fraud-detection",
        "metrics": {"Accuracy": "99.4%", "Latency": "<15ms", "Risk Engine": "Active"}
    },
    {
        "id": "sales-analysis-dashboard",
        "title": "Interactive Sales Analysis Dashboard",
        "category": "Data Analytics & Business Intelligence",
        "subtitle": "Retail Sales Performance & Profitability Optimization",
        "period": "2026",
        "technologies": ["Power BI", "DAX", "Data Modeling", "Excel", "Data Visualization"],
        "summary": "Comprehensive Business Intelligence dashboard analyzing retail sales metrics, regional distribution, and profitability levers.",
        "points": [
            "Built an interactive Power BI sales dashboard visualizing core revenue, order frequency, and regional KPIs.",
            "Uncovered strategic sales and pricing insights that directly improved overall profit margin by 15%.",
            "Implemented interactive slicing by region, product category, and temporal trends for executive leadership."
        ],
        "has_demo": True,
        "demo_type": "sales-analytics",
        "metrics": {"Profit Boost": "+15%", "KPI Tracks": "Regional & Seasonal", "Tool": "Power BI"}
    },
    {
        "id": "ai-interview-coach",
        "title": "AI Interview Coach & Evaluation System",
        "category": "Artificial Intelligence & Natural Language Processing",
        "subtitle": "Role-based Mock Interviews with Sentence Transformers & Vector DB",
        "period": "2026",
        "technologies": ["HTML", "FastAPI", "JavaScript", "MySQL", "Python", "Pandas", "Chroma DB", "Speech-to-Text", "Sentence Transformers"],
        "summary": "An intelligent voice & text AI interview platform that conducts role-tailored technical interviews, computes semantic match scores, and generates actionable candidate feedback.",
        "points": [
            "Engineered AI mock interview workflow powered by FastAPI and Sentence Transformers for semantic response evaluation.",
            "Utilized Chroma DB vector database for semantic context retrieval and technical domain knowledge matching.",
            "Integrated speech processing for real-time answer transcription, automated score reports, and strengths/weaknesses breakdowns."
        ],
        "has_demo": True,
        "demo_type": "interview-coach",
        "metrics": {"AI Scorer": "Sentence Transformers", "Vector Store": "Chroma DB", "Feedback": "Real-time"}
    }
]

EDUCATION_DATA = [
    {
        "degree": "B.Tech — Computer Science & Engineering (Data Science)",
        "institution": "Dr. A.P.J. Abdul Kalam Technical University (AKTU)",
        "location": "Lucknow, Uttar Pradesh, India",
        "period": "2023 – 2027 (Expected)",
        "highlights": [
            "Specialization in Data Science, Machine Learning Algorithms, and Advanced Database Systems.",
            "Active developer & researcher in AI/ML solutions, FastAPI application architecture, and Data Analytics."
        ]
    }
]

CERTIFICATIONS_DATA = [
    {
        "title": "Certificate of Participation — GEN AI Exchange Hackathon 2025",
        "issuer": "Google Cloud",
        "date": "2025",
        "badge": "Generative AI",
        "description": "Participated in designing generative AI solution architecture using Google Cloud ecosystem tools."
    },
    {
        "title": "Certificate of Participation — Solution Challenge 2026",
        "issuer": "Google Developer Student Clubs / Solution Challenge",
        "date": "2026",
        "badge": "Prototype Winner",
        "description": "Awarded certificate for building a successful real-world software prototype solving community challenges."
    },
    {
        "title": "Data Analyst Participation Certificate",
        "issuer": "NoviTech Pvt. Ltd",
        "date": "2026",
        "badge": "Data Analysis",
        "description": "Hands-on training and project completion in statistical data analysis, visualization, and reporting."
    },
    {
        "title": "Certificate of Internship in AI Data Analytics",
        "issuer": "In Amigos Foundation",
        "date": "July 2026",
        "badge": "AI & Analytics",
        "description": "Completed internship focused on AI-powered dataset analysis and business insight generation."
    },
    {
        "title": "Certificate of Internship in Python Development",
        "issuer": "Client Code AI Innovation Pvt. Ltd",
        "date": "July 2026",
        "badge": "Python Engineering",
        "description": "Completed internship developing production-grade Python backend applications and APIs."
    }
]
