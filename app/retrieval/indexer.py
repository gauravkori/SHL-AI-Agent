import json
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="chroma_db")

try:
    client.delete_collection("shl_catalog")
except Exception:
    pass

collection = client.create_collection("shl_catalog")


def build_index():
    with open("data/assessments.json", "r", encoding="utf-8") as f:
        assessments = json.load(f)

    ids = []
    docs = []
    metadatas = []

    for item in assessments:

        text = f"""
Assessment Name: {item.get("name", "")}

Description:
{item.get("description", "")}

Job Levels:
{", ".join(item.get("job_levels", []))}

Duration:
{item.get("duration", "")}

Remote:
{item.get("remote", "")}

Adaptive:
{item.get("adaptive", "")}

Languages:
{", ".join(item.get("languages", []))}

Categories:
{", ".join(item.get("keys", []))}
"""

        ids.append(str(item.get("entity_id")))
        docs.append(text)

        metadatas.append({
            "name": item.get("name", ""),
            "url": item.get("link", ""),
            "duration": item.get("duration", ""),
            "remote": item.get("remote", ""),
            "adaptive": item.get("adaptive", ""),
            "description": item.get("description", ""),
            "job_levels": ", ".join(item.get("job_levels", [])),
            "languages": ", ".join(item.get("languages", [])),
            "categories": ", ".join(item.get("keys", []))
        })

    print("Generating embeddings...")

    embeddings = model.encode(
        docs,
        convert_to_numpy=True,
        show_progress_bar=True
    ).tolist()

    print("Saving into ChromaDB...")

    collection.add(
        ids=ids,
        documents=docs,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"✅ Indexed {len(ids)} assessments successfully!")