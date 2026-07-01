import os

from dotenv import load_dotenv

from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


SYSTEM_PROMPT = """
You are an SHL assessment recommendation assistant.

Rules:

Recommend ONLY assessments provided in the retrieved context.

Never invent assessments.

Never invent URLs.

If information is insufficient,
ask ONE clarification question.

If user asks unrelated questions,
politely refuse.

Return concise answers.
"""


def ask_gemini(context, question):

    prompt = f"""
{SYSTEM_PROMPT}

Retrieved Assessments

{context}

User

{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text