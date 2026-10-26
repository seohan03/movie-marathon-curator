
import chromadb
import json
from pathlib import Path

# STEP 1: Create a persistent database
client = chromadb.PersistentClient(path="./chroma_db")

# STEP 2: Create a collection for our movies
collection = client.get_or_create_collection(
    name="movies"
)

# STEP 3: Load the first 5 movies
movies = []

with open("data/movies_600.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        movies.append(json.loads(line))

        if len(movies) == 600:
            break

# STEP 4: Store movies in ChromaDB
for movie in movies:
    collection.upsert(
        ids=[movie["id"]],
        documents=[movie["summary"]],
        metadatas=[{"title": movie["title"]}]
    )

    print("Added:", movie["title"])

print("\nTotal movies in database:", collection.count())
