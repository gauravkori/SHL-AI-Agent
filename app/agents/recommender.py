from app.memory import (
    add_message,
    get_profile,
    save_profile,
)

from app.retrieval.retriever import retrieve
from app.utils.gemini_client import ask_gemini
from app.agents.conversation_manager import (
    next_missing_field,
    clarification_question,
)


def chat(session_id: str, message: str):

    message = message.strip()

    add_message(session_id, "user", message)

    profile = get_profile(session_id)

    # -----------------------------
    # Conversation Manager
    # -----------------------------

    missing = next_missing_field(profile)

    # First message -> save role
    if missing == "role":

        save_profile(session_id, "role", message)

        return {
            "reply": clarification_question("experience"),
            "recommendations": [],
            "end_of_conversation": False
        }

    # Second message -> save experience
    if missing == "experience":

        save_profile(session_id, "experience", message)

        profile = get_profile(session_id)

    # -----------------------------
    # Build Search Query
    # -----------------------------

    query = f"""
Role:
{profile.get("role","")}

Experience:
{profile.get("experience","")}
"""

    # -----------------------------
    # Retrieve Assessments
    # -----------------------------

    retrieved = retrieve(query, k=5)

    context = ""

    recommendations = []

    for item in retrieved:

        context += f"""
Assessment Name:
{item['name']}

Description:
{item['description']}

Duration:
{item['duration']}

Job Levels:
{item['job_levels']}

Languages:
{item['languages']}

Remote:
{item['remote']}

Adaptive:
{item['adaptive']}

Categories:
{item['categories']}

URL:
{item['url']}

----------------------------------------
"""

        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "duration": item["duration"],
            "job_levels": item["job_levels"],
            "languages": item["languages"],
            "remote": item["remote"],
            "adaptive": item["adaptive"],
            "categories": item["categories"]
        })

    # -----------------------------
    # Gemini
    # -----------------------------

    reply = ask_gemini(
        context=context,
        question=query
    )

    add_message(session_id, "assistant", reply)

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": False
    }