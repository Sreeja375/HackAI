import streamlit as st

from modules.idea_generator import generate_idea
from modules.task_planner import generate_tasks
from modules.liked_projects import like_project, get_liked_projects

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(page_title="HackMate AI", layout="centered")

st.title("🚀 HackMate AI")
st.subheader("Hackathon Idea & Project Manager")
st.markdown("Generate ideas, plan execution, and save projects you like.")

# -------------------------------------------------
# Initialize Session State
# -------------------------------------------------
if "idea" not in st.session_state:
    st.session_state.idea = None

if "liked_projects" not in st.session_state:
    st.session_state.liked_projects = []

# -------------------------------------------------
# User Inputs
# -------------------------------------------------
domain = st.selectbox(
    "Select hackathon domain",
    ["Healthcare", "Education", "Climate", "Productivity"]
)

project_type = st.selectbox(
    "Select project type",
    ["AI", "Web"]
)

# -------------------------------------------------
# Generate Idea
# -------------------------------------------------
if st.button("💡 Generate Idea"):
    st.session_state.idea = generate_idea(domain)

# -------------------------------------------------
# Display Idea and Task Plan
# -------------------------------------------------
if st.session_state.idea:
    st.success("💡 Generated Hackathon Idea")
    st.write(st.session_state.idea)

    # ❤️ Like Project Feature
    if st.button("❤️ Like this project"):
        st.session_state.liked_projects, msg = like_project(
            st.session_state.liked_projects,
            st.session_state.idea
        )
        st.info(msg)

    st.success("🗂 Suggested Task Plan")
    tasks = generate_tasks(project_type)
    for i, task in enumerate(tasks, 1):
        st.write(f"{i}. {task}")

# -------------------------------------------------
# Show Liked Projects
# -------------------------------------------------
liked = get_liked_projects(st.session_state.liked_projects)

if liked:
    st.subheader("❤️ Liked Projects")
    for idx, project in enumerate(liked, 1):
        st.write(f"{idx}. {project}")
