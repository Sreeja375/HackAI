def generate_tasks(project_type):
    tasks = {
        "ai": [
            "Collect dataset",
            "Build baseline model",
            "Evaluate results",
            "Prepare demo"
        ],
        "web": [
            "Design UI",
            "Implement frontend",
            "Connect backend",
            "Deploy app"
        ]
    }

    return tasks.get(project_type.lower(), ["Plan", "Build", "Test", "Deploy"])
