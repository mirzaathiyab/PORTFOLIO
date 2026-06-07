"""
Portfolio Website - Mirza Athiyab Baig
Flask Application
"""

from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'mirza_portfolio_secret_key'

# Configuration
app.config['UPLOAD_FOLDER'] = 'static'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Project data
projects = [
    {
        'id': 1,
        'title': 'AI-Powered Career Guidance System',
        'description': 'An intelligent career counseling system that suggests career paths based on user skills, interests, and market trends using Machine Learning algorithms.',
        'technologies': ['Flask', 'Machine Learning', 'Python', 'HTML/CSS'],
        'github': 'https://github.com/mirzaathiyab/AI-Powered-Career-Guidance-Skill-Assessment-System',
        'category': 'ml'
    },
    {
        'id': 2,
        'title': 'CyberGuard',
        'description': 'A cybersecurity threat detection system using Random Forest classifier and Mixed Integer Programming for enhanced network security.',
        'technologies': ['Random Forest', 'MIP', 'Python', 'Cybersecurity'],
        'github': 'https://github.com/mirzaathiyab/Cyber-Hacking-Breaches',
        'category': 'ml'
    },
    {
        'id': 3,
        'title': 'Fake News Detection',
        'description': 'NLP-based application to detect fake news articles using TF-IDF vectorization and Logistic Regression classifier.',
        'technologies': ['TF-IDF', 'Logistic Regression', 'NLP', 'Python'],
        'github': 'https://github.com/mirzaathiyab/MIRZA-ATHIYAB-BAIG__EDULUMOS-INTERNSHIP-TASKS/tree/main/MIRZA%20ATHIYAB%20BAIG%20EDULUMOS%20TASK%204',
        'category': 'nlp'
    },
    {
        'id': 4,
        'title': 'WanderMate AI Trip Planner',
        'description': 'An AI-powered travel planning application that creates personalized itineraries based on preferences, budget, and travel dates.',
        'technologies': ['Flask', 'AI/ML', 'Python', 'JavaScript'],
        'github': 'https://github.com/mirzaathiyab',
        'category': 'web'
    },
    {
        'id': 5,
        'title': 'Smart Study Score Predictor',
        'description': 'Machine learning model to predict student academic performance based on various factors like study hours, attendance, and previous scores.',
        'technologies': ['Python', 'Scikit-learn', 'Flask', 'Pandas'],
        'github': 'https://github.com/mirzaathiyab/MIRZA-ATHIYAB-BAIG__EDULUMOS-INTERNSHIP-TASKS/tree/main/MIRZA%20ATHIYAB%20BAIG%20EDULUMOS%20TASK1',
        'category': 'ml'
    },
    {
        'id': 6,
        'title': 'EduIQ Student Progress Analysis',
        'description': 'Comprehensive student performance analytics dashboard with visualization and predictive insights for educational institutions.',
        'technologies': ['Python', 'Power BI', 'Tableau', 'Data Analysis'],
        'github': 'https://github.com/mirzaathiyab',
        'category': 'web'
    }
]

# Experience data
experiences = [
    {
        "title": "Machine Learning Intern",
        "company": "EduLumos",
        "duration": "Present",
        "description": "Developing machine learning models for educational analytics.",
        "skills": ["Python", "Scikit-Learn", "Pandas", "Machine Learning"],
        "logo": "edulumos.png"
    },
    {
        "title": "CyberGuard Internship",
        "company": "Manac InfoTech Ltd",
        "duration": "Past",
        "description": "Worked on cybersecurity threat detection using ML.",
        "skills": ["Cybersecurity", "Machine Learning", "Data Analysis"],
        "logo": "manac.png"
    },
    {
        "title": "Data Science Intern",
        "company": "YHills",
        "duration": "Past",
        "description": "Built predictive models and business insights.",
        "skills": ["Python", "Data Science", "Analytics"],
        "logo": "yhills.png"
    }
];

# Certifications data
certifications = [
    {
        'title': 'IBM Data Fundamentals',
        'issuer': 'IBM',
        'description': 'Foundation-level certification in data science fundamentals, data visualization, and analytics.'
    },
    {
        'title': 'Oracle Certified AI Foundations Associate',
        'issuer': 'Oracle',
        'description': 'Certification in AI concepts, machine learning fundamentals, and AI applications.'
    },
    {
        'title': 'Oracle Certified Data Science Professional',
        'issuer': 'Oracle',
        'description': 'Professional certification in data science methodologies, algorithms, and practical applications.'
    },
    {
        'title': 'Power BI Certification',
        'issuer': 'Arasmo Technologies ',
        'description': 'Certification in business intelligence, data visualization, and dashboard creation using Power BI.'
    },
    {
        'title': 'Python for Data Science',
        'issuer': 'Various',
        'description': 'Comprehensive Python programming certification focused on data science applications.'
    },
    {
        'title': 'Web Development using AI',
        'issuer': 'Internshala Trainings',
        'description': 'Learning to integrate AI models into web applications to build intelligent and interactive features. '
    }
]

# Achievements data
achievements = [
    {
        'title': '1st Prize – HackWeb Hackathon',
        'description': 'Won first place in HackWeb Hackathon for developing an innovative AI solution.'
    },
    {
        'title': 'Tata Data Analytics Virtual Internship',
        'description': 'Completed virtual internship program at Tata on data analytics and visualization.'
    },
    {
        'title': 'Deloitte Data Analytics Virtual Internship',
        'description': 'Completed virtual internship at Deloitte focusing on data analytics and business insights.'
    },
    {
        'title': 'Event Appreciation – Sanketika & Datanova',
        'description': 'Received appreciation for outstanding contributions in technical events and data science competitions.'
    }
]

# Skills data
skills = [
    {'name': 'Python', 'level': 90, 'category': 'language'},
    {'name': 'Machine Learning', 'level': 85, 'category': 'ml'},
    {'name': 'Flask', 'level': 80, 'category': 'framework'},
    {'name': 'SQL', 'level': 75, 'category': 'language'},
    {'name': 'Power BI', 'level': 80, 'category': 'tool'},
    {'name': 'Tableau', 'level': 75, 'category': 'tool'},
    {'name': 'NumPy', 'level': 85, 'category': 'library'},
    {'name': 'Pandas', 'level': 85, 'category': 'library'},
    {'name': 'NLP', 'level': 75, 'category': 'ml'},
    {'name': 'Java', 'level': 70, 'category': 'language'},
    {'name': 'HTML/CSS', 'level': 80, 'category': 'language'},
    {'name': 'Data Preprocessing', 'level': 85, 'category': 'skill'}
]

# Contact form handler
contacts = []

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html', 
                         projects=projects,
                         experiences=experiences,
                         certifications=certifications,
                         achievements=achievements,
                         skills=skills)

@app.route('/projects')
def projects_page():
    """Projects page route"""
    return render_template('projects.html', projects=projects)

@app.route('/experience')
def experience_page():
    """Experience page route"""
    return render_template('experience.html', experiences=experiences)

@app.route('/certifications')
def certifications_page():
    """Certifications page route"""
    return render_template('certifications.html', certifications=certifications)

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    """Contact page route with form handling"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        if name and email and message:
            contact = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
            }
            contacts.append(contact)
            flash('Thank you for your message! I will get back to you soon.', 'success')
            return redirect(url_for('contact_page'))
        else:
            flash('Please fill in all required fields.', 'error')
    
    return render_template('contact.html')

@app.route('/download-resume')
def download_resume():
    """Resume download route"""
    try:
        return send_file('resume.pdf', as_attachment=True)
    except FileNotFoundError:
        flash('Resume not found. Please contact me directly.', 'error')
        return redirect(url_for('index'))

@app.route('/filter-projects/<category>')
def filter_projects(category):
    """Filter projects by category"""
    if category == 'all':
        filtered = projects
    else:
        filtered = [p for p in projects if p.get('category') == category]
    return render_template('projects.html', projects=filtered, active_filter=category)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
