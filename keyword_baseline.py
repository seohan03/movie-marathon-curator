
import chromadb
import re

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="movies")

# Same query used for semantic search
query = (
    "Two adolescents with contrasting temperaments "
    "build a lasting bond amid social exclusion."
)

# Meaningful keywords from the query
keywords = {
    "adolescents", "contrasting", "temperaments",
    "lasting", "bond", "social", "exclusion"
}

# Retrieve all stored movie summaries
movies = collection.get(
    include=["documents", "metadatas"]
)

scores = []

for summary, metadata in zip(
    movies["documents"],
    movies["metadatas"]
):
    words = set(re.findall(r"[a-z]+", summary.lower()))

    matches = keywords & words

    scores.append((
        len(matches),
        metadata["title"],
        sorted(matches)
    ))

# Rank movies by number of matching keywords
scores.sort(key=lambda movie: movie[0], reverse=True)

print("=== KEYWORD SEARCH RESULTS ===")

for score, title, matches in scores[:5]:
    print(f"\n{title}")
    print("Matching keywords:", matches)
    print("Score:", score)

# Check our semantic search candidate
print("\n=== MINA TANNENBAUM ===")

for score, title, matches in scores:
    if title == "Mina Tannenbaum":
        print("Keyword score:", score)
        print("Matching keywords:", matches)
        break
