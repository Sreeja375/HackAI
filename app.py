import streamlit as st
from modules.idea_generator import generate_idea
from modules.task_planner import generate_tasks
from modules.liked_ideas import like_project, unlike_project, get_liked_projects
from modules.idea_evaluation import evaluate_idea

st.set_page_config(page_title="HackMate AI", layout="wide")

# ----------------- CSS -----------------
st.markdown("""
<style>
.main { background-color: #f9fafb; }
.card {
    background-color: white;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ----------------- Header -----------------
st.title("🚀 HackMate AI")
st.caption("A smart companion to generate, evaluate, and shortlist hackathon ideas")

# ----------------- Session State -----------------
if "idea" not in st.session_state:
    st.session_state.idea = None
if "liked_projects" not in st.session_state:
    st.session_state.liked_projects = []

# ----------------- Sidebar -----------------
with st.sidebar:
    st.header("⚙️ Settings")
    domain = st.selectbox(
        "Hackathon Domain",
        ["Healthcare", "Education", "Climate", "Productivity"]
    )
    project_type = st.selectbox(
        "Project Type",
        ["AI", "Web"]
    )
    st.markdown("---")
    st.markdown("💡 *Choose domain and generate ideas*")

# ----------------- Generate Idea -----------------
if st.button("✨ Generate New Idea"):
    st.session_state.idea = generate_idea(domain)

# ----------------- Main Content -----------------
col1, col2 = st.columns([2, 1])

with col1:
    if st.session_state.idea:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("💡 Generated Idea")
        st.write(st.session_state.idea)

        c1, c2 = st.columns(2)
        with c1:
            if st.button("❤️ Like Idea"):
                st.session_state.liked_projects, msg = like_project(
                    st.session_state.liked_projects,
                    st.session_state.idea
                )
                st.success(msg)
        with c2:
            if st.button("🗑 Unlike Idea"):
                st.session_state.liked_projects, msg = unlike_project(
                    st.session_state.liked_projects,
                    st.session_state.idea
                )
                st.warning(msg)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🗂 Task Plan")
        tasks = generate_tasks(project_type)
        for i, task in enumerate(tasks, 1):
            st.write(f"🔹 {task}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📊 Idea Evaluation")

        innovation = st.slider("Innovation", 1, 5, 3)
        feasibility = st.slider("Feasibility", 1, 5, 3)
        impact = st.slider("Impact", 1, 5, 3)

        if st.button("Evaluate Idea"):
            result = evaluate_idea(innovation, feasibility, impact)
            st.metric("Total Score", f"{result['total']} / 15")
            st.info(result["label"])
        st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("❤️ Liked Projects")
    liked = get_liked_projects(st.session_state.liked_projects)

    if liked:
        for i, proj in enumerate(liked, 1):
            st.write(f"{i}. {proj}")
    else:
        st.caption("No liked projects yet")
    st.markdown("</div>", unsafe_allow_html=True)
