def evaluate_idea(innovation, feasibility, impact):
    """
    Calculate total score and evaluation label for a hackathon idea.
    Each parameter is expected to be between 1 and 5.
    """

    total = innovation + feasibility + impact

    if total >= 13:
        label = "🔥 Excellent – Strong winning potential"
    elif total >= 9:
        label = "✅ Good – Worth developing"
    else:
        label = "⚠ Needs Improvement"

    return {
        "innovation": innovation,
        "feasibility": feasibility,
        "impact": impact,
        "total": total,
        "label": label
    }
