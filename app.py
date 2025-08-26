from flask import Flask, render_template

app = Flask(__name__)

# Sample data based on your resume
profile_data = {
    "name": "Gulla Naga Poojitha",
    "phone": "6305338861",
    "email": "gullanagapoojitha@gmail.com",
    "linkedin": "https://www.linkedin.com/in/naga-poojitha-gulla-110038297/",
    "github": "https://github.com/Naga-Poojitha",
    "website": "https://sites.google.com/view/academicskillshub",
    "objective": "As a highly motivated and adaptable 3rd-year B.Tech student specializing in Artificial Intelligence and Machine Learning, I aim to leverage my hands-on experience in real-time AI applications, embedded systems, and computer vision technologies like YOLOv8, Arduino, and MediaPipe to contribute to innovative, impact-driven solutions. Passionate about solving real-world problems through technology, I seek opportunities that challenge me to grow, collaborate, and deliver meaningful outcomes in AI-powered systems and smart automation."
}

education_data = [
    {
        "year": "2023 - 2027",
        "qualification": "B.Tech in Artificial Intelligence & Machine Learning",
        "institute": "Avanthi Institute of Engineering & Technology",
        "score": "81.11%"
    },
    {
        "year": "2021 - 2023",
        "qualification": "Intermediate (MPC)",
        "institute": "Sri Chaitanya Junior Kalasala",
        "score": "84.1%"
    },
    {
        "year": "2020 - 2021",
        "qualification": "SSC",
        "institute": "Sri Chaitanya School",
        "score": "99%"
    }
]

internship_data = [
    {
        "period": "2025 (July – August)",
        "role": "Intern – AI & Cloud Technologies",
        "company": "IBM SkillsBuild",
        "description": "Gained hands-on experience in AI, Cloud, and Data Analytics through IBM Cloud and mentor-led sessions."
    },
    {
        "period": "2025 (May – July)",
        "role": "Intern – Artificial Intelligence",
        "company": "Skill Dunia with Odcet Technologies",
        "description": "Completed a 3-month internship exploring AI & ML concepts through practical tasks and mini-projects."
    },
    {
        "period": "July 2025",
        "role": "Data Analytics Virtual Intern",
        "company": "TATA Forage – Job Simulation",
        "description": "Performed real-world data analytics tasks like EDA and prediction modeling in a simulated environment."
    }
]

skills_data = {
    "programming": ["Python", "C", "C++ (for Arduino)", "HTML/CSS (Basics)"],
    "tools": ["Power BI", "PyCharm", "Arduino IDE", "Visual Studio"],
    "platforms": ["YOLOv8", "Google Cloud Skills", "OpenCV", "Mediapipe"],
    "soft_skills": ["Problem Solving", "Team Collaboration", "Tech Adaptability", "Fast Learner", "Leadership", "English Proficiency (Written & Spoken)"]
}

projects_data = [
    {
        "title": "Object Detection using YOLOv8 (Python)",
        "description": "Developed a high-performance object tracking system using YOLOv8, OpenCV, and Python. Achieved real-time detection accuracy (~85%) on custom datasets with consistent frame rates."
    },
    {
        "title": "Auto Sense Mini Car (C++) – IR Sensor-Based Autonomous Car using Arduino",
        "description": "Designed and built a smart mini car using IR sensors and Arduino Uno for obstacle detection and avoidance. Achieved 90%+ accuracy in obstacle detection across varying light and surface conditions."
    },
    {
        "title": "Gesture-Controlled Game Interface using MediaPipe (Python)",
        "description": "Built a vision-based hand gesture recognition system to interact with games using real-time input. Leveraged MediaPipe and OpenCV to detect and classify gestures with high responsiveness."
    }
]

achievements_data = [
    "2nd Prize – Power BI Hackathon",
    "2nd Prize – GYAN Tech Fest Project Expo",
    "Top 5 Finalist – AI Hackathon, Siddhartha Engineering College",
    "Top 3 – ITYUKTA Tech Fest, JNTUGV",
    "1st Prize – College Chess Tournament",
    "3rd Prize – College Rubik's Cube Competition",
    "Volunteer – Street Cause Organization [NGO] (2024–2025)",
    "Member – College Dildes Club",
    "NSS Coordinator – Avanthi Institute of Engineering & Technology"
]

certifications_data = [
    "MS Office - Data Pro, Visakhapatnam (Jul – Sep 2023)",
    "Programming with Python - Internshala (May 2024 – Jun 2024) Scored 100% in the final assessment and ranked as a top performer",
    "Certificate of Merit - Awarded for my performance in a 5-Day Workshop + 24-Hour Hackathon on Power BI",
    "Participation Certificate - GYAN 2K24 - Represented my department at this National Level AI Tech Fest",
    "AI Autonomous Hackathon 2025 - Project Expo, Secured Runner-up in a Project Expo at GYAN 2K24",
    "AI Autonomous Hackathon 2025 - Theme: AI Game Changers Participated in a national-level hackathon",
    "ITYUKTA 2K25 - JNTUGV Vizianagaram, Participated in a Project Expo at this national-level tech symposium"
]

@app.route('/')
def index():
    return render_template('index.html', profile=profile_data)

@app.route('/education')
def education():
    return render_template('education.html', profile=profile_data, education=education_data)

@app.route('/experience')
def experience():
    return render_template('experience.html', profile=profile_data, internships=internship_data, certifications=certifications_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', profile=profile_data, projects=projects_data)

@app.route('/skills')
def skills():
    return render_template('skills.html', profile=profile_data, skills=skills_data)

@app.route('/achievements')
def achievements():
    return render_template('achievements.html', profile=profile_data, achievements=achievements_data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
