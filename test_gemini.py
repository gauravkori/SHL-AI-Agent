from app.utils.gemini_client import ask_gemini

answer = ask_gemini(
    "Reply with exactly these words: Gemini Connected Successfully"
)

print(answer)