import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("shl_catalog")


def retrieve(query: str, k: int = 5):
    """
    Retrieve the top-k most relevant SHL assessments
    using semantic search.
    """

    embedding = model.encode(
        query,
        convert_to_numpy=True
    ).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=k
    )

    recommendations = []

    metadatas = results["metadatas"][0]
    documents = results["documents"][0]

    for metadata, document in zip(metadatas, documents):

        recommendations.append({
            "name": metadata.get("name", ""),
            "url": metadata.get("url", ""),
            "duration": metadata.get("duration", ""),
            "remote": metadata.get("remote", ""),
            "adaptive": metadata.get("adaptive", ""),
            "description": metadata.get("description", ""),
            "job_levels": metadata.get("job_levels", ""),
            "languages": metadata.get("languages", ""),
            "categories": metadata.get("categories", ""),
            "content": document
        })

    return recommendations