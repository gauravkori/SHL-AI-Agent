REQUIRED_FIELDS = [
    "role",
    "experience"
]


def next_missing_field(profile: dict):
    """
    Returns the next missing field required
    before recommending assessments.
    """

    for field in REQUIRED_FIELDS:
        if field not in profile or not profile[field]:
            return field

    return None


def clarification_question(field: str):

    questions = {
        "role": "What role are you hiring for?",
        "experience": "What experience level are you hiring for? (Entry-Level, Mid-Professional, Senior Leadership)"
    }

    return questions.get(field)