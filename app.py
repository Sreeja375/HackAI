from modules.idea_generator import generate_idea
from modules.task_planner import generate_tasks

if __name__ == "__main__":
    domain = "healthcare"
    project_type = "ai"

    print("💡 Hackathon Idea:")
    print(generate_idea(domain))

    print("\n🗂 Task Plan:")
    for i, task in enumerate(generate_tasks(project_type), 1):
        print(f"{i}. {task}")
