import streamlit as st
from modules.idea_generator import generate_idea
from modules.task_planner import generate_tasks
from modules.readme_generator import generate_readme


st.set_page_config(page_title="HackMate AI", layout="centered")

st.title("🚀 HackMate AI")
st.subheader("Your Hackathon Companion")

st.markdown("Generate ideas and plan tasks in seconds.")

# User inputs
domain = st.selectbox(
    "Select hackathon domain",
    ["Healthcare", "Education", "Climate", "Productivity"]
)

project_type = st.selectbox(
    "Select project type",
    ["AI", "Web"]
)

if st.button("Generate Plan"):
    st.success("💡 Hackathon Idea")
    st.write(generate_idea(domain))

    st.success("🗂 Task Plan")
    tasks = generate_tasks(project_type)
    for i, task in enumerate(tasks, 1):
        st.write(f"{i}. {task}")
if st.button("📄 Generate README"):
    st.success("📘 Auto-Generated README")
    st.code(
        generate_readme("HackMate AI", st.session_state.idea),
        language="markdown"
    )

