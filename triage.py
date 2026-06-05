def classify_bug(bug):
    bug = bug.lower()

    if "crash" in bug or "error" in bug:
        priority = "High"
        category = "Backend"
        team = "Backend Team"

    elif "slow" in bug or "delay" in bug:
        priority = "Medium"
        category = "Performance"
        team = "Optimization Team"

    else:
        priority = "Low"
        category = "UI"
        team = "Frontend Team"

    return {
        "category": category,
        "priority": priority,
        "assigned_to": team
    }