import json
import re

INPUT = "data/assessments.json"
OUTPUT = "data/assessments_fixed.json"

with open(INPUT, "r", encoding="utf-8") as f:
    text = f.read()

# Replace illegal newlines inside quoted strings
pattern = r'"(?:[^"\\]|\\.)*"'

def clean(match):
    s = match.group(0)
    s = s.replace("\n", " ")
    s = s.replace("\r", " ")
    return s

fixed = re.sub(pattern, clean, text)

# Validate
data = json.loads(fixed)

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("SUCCESS")
print("Records:", len(data))