def like_project(liked_projects, idea):
    """
    Save a project idea if not already liked.
    """
    if idea and idea not in liked_projects:
        liked_projects.append(idea)
        return liked_projects, "Project added to liked list ❤️"
    elif idea in liked_projects:
        return liked_projects, "Project already liked 👍"
    else:
        return liked_projects, "No project to like"


def get_liked_projects(liked_projects):
    """
    Return all liked project ideas.
    """
    return liked_projects
