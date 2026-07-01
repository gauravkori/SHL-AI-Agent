from app.retrieval.retriever import retrieve

results = retrieve("Java backend developer")

for i, assessment in enumerate(results, start=1):
    print("=" * 60)
    print(f"Result {i}")
    print("=" * 60)
    print("Name       :", assessment["name"])
    print("Duration   :", assessment["duration"])
    print("Job Levels :", assessment["job_levels"])
    print("Languages  :", assessment["languages"])
    print("Remote     :", assessment["remote"])
    print("Adaptive   :", assessment["adaptive"])
    print("Categories :", assessment["categories"])
    print("URL        :", assessment["url"])
    print()