from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

# Your portfolio data
PROFILE_DATA = {
    'name': 'Vignesh',
    'title': 'Full-Stack Developer & Commerce Enthusiast',
    'email': 'vickyapjlove@gmail.com',
    'phone': '+91 8428591065',
    'location': 'Coimbatore, India',
    'about': {
        'intro': "I'm a passionate Full-Stack Developer with a unique blend of technical expertise and business acumen from my B.Com background.",
        'details': [
            "I create modern, scalable web applications that bridge technology and business needs.",
            "My commerce background gives me exceptional analytical skills for understanding client requirements.",
            "I excel at turning complex problems into elegant, user-friendly solutions."
        ]
    },
    'education': [
        {
            'institution': 'KPR College of Arts, Science and Research',
            'degree': 'B.Com (Computer Applications)',
            'period': '2023 – 2026',
            'status': 'Pursuing',
            'achievements': ['Current CGPA: 8.5/10', 'Active in coding competitions']
        },
        {
            'institution': 'Holy Cross Matric Higher Secondary School',
            'degree': 'HSC (Commerce with Computer Applications)',
            'period': '2022 – 2023',
            'status': 'Completed',
            'achievements': ['Scored 97%', 'School Topper in Computer Science']
        }
    ],
    'skills': {
        'Frontend': ['HTML5', 'CSS3', 'JavaScript', 'React', 'Vue.js', 'Bootstrap', 'Tailwind CSS'],
        'Backend': ['Python', 'Flask', 'Django', 'PHP', 'Node.js', 'RESTful APIs'],
        'Database': ['MySQL', 'PostgreSQL', 'SQLite', 'MongoDB'],
        'Tools': ['Git', 'Docker', 'Twilio API', 'AWS', 'VS Code', 'Postman']
    },
    'projects': [
        {
            'id': 1,
            'title': 'Visitor Management System',
            'description': 'A comprehensive security system with Twilio SMS integration and MySQL database for real-time visitor tracking and notifications.',
            'full_description': 'Developed a complete visitor management solution featuring real-time SMS alerts to hosts, visitor registration, digital check-ins, and detailed reporting. Integrated Twilio API for seamless communication and deployed on cloud infrastructure.',
            'technologies': ['PHP', 'MySQL', 'Twilio API', 'JavaScript', 'Bootstrap'],
            'features': ['Real-time SMS alerts', 'Visitor analytics', 'Host notifications', 'Secure data storage'],
            'github': 'https://github.com/Vickyvkz7/visitor-management',
            'live': '#',
            'image': '1.png',
            'category': 'Full Stack'
        },
        {
            'id': 2,
            'title': 'Student Career Guidance Platform (One Step)',
            'description': 'A comprehensive educational portal addressing low enrollment and dropout rates in Jammu & Kashmir through personalized career guidance and college mapping.',
            'full_description': 'Developed an intelligent platform to help parents and students make well-informed decisions about education and careers. The portal offers interest tests, course-to-career mapping, a local college directory, and personalized advice. Features include AI-driven career chatbots, career quizzes, student and parent dashboards, financial planning tools, quota information, offline SMS notifications, internship opportunities, entrance exam preparation, and admission alerts. The system successfully targets reducing dropout rates from high levels to 90% enrollment and promoting equal educational opportunities across the region.',
            'technologies': ['Python', 'Flask', 'HTML/CSS', 'Jinja2', 'Bootstrap', 'AI Chatbot', 'MySQL'],
            'features': ['Interest tests', 'Course-to-career mapping', 'Local college directory', 'AI career chatbots', 'Career quizzes', 'Student dashboards', 'Parent dashboards', 'Financial planning tools', 'Quota information', 'Offline SMS notifications', 'Internship opportunities', 'Entrance exam preparation', 'Admission alerts', 'Profile management'],
            'github': 'https://github.com/Vickyvkz7/career-guidance',
            'live': '#',
            'image': 'education.png',
            'category': 'Full Stack'
        }
    ],
    'achievements': [
        {
            'title': 'Academic Excellence',
            'description': 'Consistently maintained outstanding academic performance with 97% in HSC',
            'icon': 'trophy'
        },
        {
            'title': 'Hackathon Winner',
            'description': 'Won multiple hackathons by building innovative web applications',
            'icon': 'code'
        },
        {
            'title': 'Full-Stack Expertise',
            'description': 'Proven ability to deliver end-to-end web solutions',
            'icon': 'layers'
        }
    ],
    'social_links': {
        'github': 'https://github.com/Vickyvkz7',
        'linkedin': 'https://www.linkedin.com/in/vicky-vignesh-613159283',
        'email': 'vickyapjlove@gmail.com'
    }
}

@app.route('/')
def index():
    return render_template('index.html', profile=PROFILE_DATA)

@app.route('/about')
def about():
    return render_template('about.html', profile=PROFILE_DATA)

@app.route('/projects')
def projects():
    return render_template('projects.html', profile=PROFILE_DATA)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        try:
            # Send email notification
            msg = Message(
                subject=f"Portfolio Contact: {subject}",
                recipients=[PROFILE_DATA['email']],
                body=f"""
Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
                """
            )
            mail.send(msg)
            flash('Your message has been sent successfully! I\'ll get back to you soon.', 'success')
        except Exception as e:
            flash('Sorry, there was an error sending your message. Please try again later.', 'error')
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html', profile=PROFILE_DATA)

if __name__ == '__main__':
    app.run(debug=True)