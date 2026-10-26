
import chromadb

# Connect to the saved database
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="movies")

# Ask the user for a movie description
query = input("What kind of movie are you looking for? ")

# Search by semantic meaning
results = collection.query(
    query_texts=[query],
    n_results=5
)

# Display the recommendations
for i, metadata in enumerate(results["metadatas"][0]):
    print(f"\n{i + 1}. {metadata['title']}")
    print("Distance:", results["distances"][0][i])
    print("Plot:", results["documents"][0][i][:200])
