import random

IDEAS = {
    "healthcare": [
        "AI-powered symptom checker with explainable results",
        "Emergency SOS app with auto location and medical info sharing",
        "Mental health burnout detector using daily habit inputs",
        "Smart medication reminder with drug–drug interaction alerts",
        "AI healthcare chatbot for rural and remote areas",
        "Hospital queue and appointment management system",
        "Women safety and health monitoring application",
        "AI-based diet and lifestyle planner",
        "Post-surgery recovery tracking assistant",
        "Disease outbreak early warning system using AI"
    ],

    "climate": [
        "Carbon footprint tracker with personalized AI recommendations",
        "Smart waste segregation using computer vision",
        "Air quality prediction and pollution alert system",
        "Water usage optimization platform",
        "Climate risk alert app for farmers",
        "Energy consumption optimization dashboard",
        "Tree plantation tracking using satellite imagery",
        "Plastic waste detection and reporting system",
        "Green commute recommendation platform",
        "Sustainable shopping recommendation app"
    ],

    "education": [
        "Personalized AI tutor for students",
        "Exam preparation planner with adaptive difficulty",
        "AI doubt-solving assistant for classrooms",
        "Skill-gap analyzer for students",
        "Career roadmap generator based on interests",
        "AI plagiarism and originality checker",
        "Smart attendance and engagement analyzer",
        "Learning style detection system",
        "AI mentor for competitive exam preparation",
        "Student mental wellness support chatbot"
    ],

    "productivity": [
        "Hackathon companion app for idea generation and planning",
        "AI task planner with smart deadline prioritization",
        "Meeting summarizer with action-item tracker",
        "AI resume analyzer and improvement assistant",
        "Startup pitch generator using AI",
        "Focus and distraction detection application",
        "Time management assistant for students",
        "Daily productivity score tracker",
        "Team collaboration and role assignment AI",
        "Code quality checker and README auto-generator"
    ]
}

def generate_idea(domain):
    domain = domain.lower()
    if domain in IDEAS:
        return random.choice(IDEAS[domain])
    return "AI-powered solution for a real-world problem"
