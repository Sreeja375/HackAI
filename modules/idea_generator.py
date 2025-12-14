def generate_idea(domain):
    ideas = {
        "healthcare": "AI-powered symptom triage and emergency alert system",
        "education": "Personalized AI tutor using learning analytics",
        "climate": "Carbon footprint tracker with AI recommendations",
        "productivity": "AI task planner for hackathons"
    }

    return ideas.get(domain.lower(), "AI-powered solution for real-world problem")
