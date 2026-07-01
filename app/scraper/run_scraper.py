import json

from app.scraper.crawler import download
from app.scraper.parser import extract_assessment
from app.scraper.exporter import save_json


with open("links.json", encoding="utf8") as f:
    links = json.load(f)

results = []

BASE = "https://www.shl.com"

for item in links:

    url = item.get("url", "")

    if not url:
        continue

    if url.startswith("/"):
        url = BASE + url

    print("Downloading:", url)

    html = download(url)

    if not html:
        continue

    data = extract_assessment(html, url)

    if data["name"]:
        results.append(data)

save_json(
    results,
    "data/assessments.json"
)