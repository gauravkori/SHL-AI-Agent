import requests
import json

url = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"

text = requests.get(url).text

print("First 200 characters:")
print(text[:200])

try:
    data = json.loads(text)
    print("✅ Valid JSON")
    print(type(data))
except Exception as e:
    print("❌ Invalid JSON")
    print(e)