def like_project(liked_projects, idea):
    """
    Add an idea to liked projects if not already present.
    """
    if idea and idea not in liked_projects:
        liked_projects.append(idea)
        return liked_projects, "Project added to liked list ❤️"
    elif idea in liked_projects:
        return liked_projects, "Project already liked 👍"
    else:
        return liked_projects, "No project to like"


def unlike_project(liked_projects, idea):
    """
    Remove an idea from liked projects.
    """
    if idea in liked_projects:
        liked_projects.remove(idea)
        return liked_projects, "Project removed from liked list 🗑"
    else:
        return liked_projects, "Project not found in liked list"


def get_liked_projects(liked_projects):
    """
    Return all liked project ideas.
    """
    return liked_projects
