from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  


PROFILE = {
    "name": "Abdallah H. Sodangu",
    "title": "Data Science Student",
    "university": "Easten Africa Statistical Training centre",
    "email": "sodangua@email.com",
    "github": "https://github.com/Abdallah01234567890",
    "linkedin": "https://linkedin.com/in/abdallah-sodangu-0436981a3/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3Br9yQRPgQRguwoePy0rwUMQ%3D%3D",
    "bio": "Mwanafunzi wa Data Science mwenye shauku katika Data analytics,web development na cloud computing."
}

SKILLS = [
    {"category": "Frontend",       "items": ["HTML5", "CSS3", "JavaScript"]},
    {"category": "Backend",        "items": ["Python", "Flask", "REST APIs"]},
    {"category": "Database",       "items": ["SQL", "MySQL", "SQLite"]},
    {"category": "Cloud & Tools",  "items": ["Git", "GitHub", "Vercel", "Render"]},
]

PROJECTS = [
    {
        "id": 1,
        "title": "Portfolio Website",
        "description": "Personal portfolio deployed on Vercel with backend on Render.",
        "tags": ["HTML/CSS", "Flask", "Vercel", "Render"],
        "github": "https://github.com/Abdallah01234567890/Portipholio-02"
    },
    {
        "id": 2,
        "title": "Student Management System",
        "description": "System ya kusimamia records za wanafunzi, built na Python na SQLite.",
        "tags": ["Python", "SQLite", "CLI"],
        "github": "https://github.com/Abdallah01234567890/Finance-Dashbord_01"
    },
    {
        "id": 3,
        "title": "Weather App",
        "description": "Web app inayofetch weather data kutoka public API.",
        "tags": ["JavaScript", "REST API", "CSS"],
        "github": "https://github.com/Abdallah01234567890/Seles-Dashbord-03"
    },
]

# ── ROUTES (Endpoints) ───────────────────────────────────────────

@app.route("/")
def home():
    """Root endpoint — inathibitisha API inafanya kazi"""
    return jsonify({
        "message": "Portfolio API inafanya kazi!",
        "endpoints": ["/api/profile", "/api/skills", "/api/projects"]
    })

@app.route("/api/profile")
def get_profile():
    """Rudisha taarifa za kibinafsi"""
    return jsonify(PROFILE)

@app.route("/api/skills")
def get_skills():
    """Rudisha orodha ya skills"""
    return jsonify(SKILLS)

@app.route("/api/projects")
def get_projects():
    """Rudisha orodha ya projects"""
    return jsonify(PROJECTS)

@app.route("/api/projects/<int:project_id>")
def get_project(project_id):
    """Rudisha project moja kwa ID yake"""
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if project:
        return jsonify(project)
    return jsonify({"error": "Project haikupatikana"}), 404

# ── RUN ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True)
