
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="movies")

results = collection.get(
    where={"title": "The Midnight Lighthouse Test"}
)

if results["ids"]:
    print("PASS: Movie survived the restart!")
else:
    print("FAIL: Movie not found.")

print("Total stored movies:", collection.count())
