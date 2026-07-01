import json

from app.models.assessment import Assessment


def load_assessments(path="data/assessments.json"):

    with open(path, "r", encoding="utf-8") as f:

        data = json.load(f)

    return [Assessment(**item) for item in data]