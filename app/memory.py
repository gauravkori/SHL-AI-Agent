from collections import defaultdict

conversation_store = defaultdict(
    lambda: {
        "messages": [],
        "clarification_stage": None,
        "user_profile": {}
    }
)


def get_session(session_id: str):
    return conversation_store[session_id]


def add_message(session_id: str, role: str, content: str):
    conversation_store[session_id]["messages"].append({
        "role": role,
        "content": content
    })


def get_messages(session_id: str):
    return conversation_store[session_id]["messages"]


def save_profile(session_id: str, key: str, value):
    conversation_store[session_id]["user_profile"][key] = value


def get_profile(session_id: str):
    return conversation_store[session_id]["user_profile"]


def set_stage(session_id: str, stage: str):
    conversation_store[session_id]["clarification_stage"] = stage


def get_stage(session_id: str):
    return conversation_store[session_id]["clarification_stage"]


def clear_session(session_id: str):
    conversation_store.pop(session_id, None)