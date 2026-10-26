import chromadb

# Reopen the existing database
client = chromadb.PersistentClient(path="./chroma_db")

# Access our saved movie collection
collection = client.get_collection(name="movies")

print("Saved movies:", collection.count())

# Retrieve one movie
results = collection.peek(limit=1)

print("Example movie:", results["metadatas"][0]["title"])
