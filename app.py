import streamlit as st
from modules.idea_generator import generate_idea
from modules.task_planner import generate_tasks
from modules.readme_generator import generate_readme

st.set_page_config(page_title="HackMate AI", layout="centered")

st.title("🚀 HackMate AI")
st.subheader("Your Hackathon Companion")
st.markdown("Generate ideas and plan tasks in seconds.")

# ✅ Initialize session state
if "idea" not in st.session_state:
    st.session_state.idea = None

# User inputs
domain = st.selectbox(
    "Select hackathon domain",
    ["Healthcare", "Education", "Climate", "Productivity"]
)

project_type = st.selectbox(
    "Select project type",
    ["AI", "Web"]
)

# Generate Plan
if st.button("Generate Plan"):
    st.session_state.idea = generate_idea(domain)

# Show idea & tasks ONLY if idea exists
if st.session_state.idea:
    st.success("💡 Hackathon Idea")
    st.write(st.session_state.idea)

    st.success("🗂 Task Plan")
    tasks = generate_tasks(project_type)
    for i, task in enumerate(tasks, 1):
        st.write(f"{i}. {task}")

# README button (always visible, but controlled)
if st.button("📄 Generate README"):
    if st.session_state.idea:
        st.success("📘 Auto-Generated README")
        st.code(
            generate_readme("HackMate AI", st.session_state.idea),
            language="markdown"
        )
    else:
        st.warning("Please generate an idea first")
