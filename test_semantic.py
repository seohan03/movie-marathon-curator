
import chromadb
import re

# Connect to our persistent movie database
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="movies")

# Our two semantic search test queries

test_queries = [
    "A reflective story about someone yearning to relive "
    "the happiness of their younger days.",

    "Two adolescents with contrasting temperaments "
    "build a lasting bond amid social exclusion."
]


# Common words that aren't useful for keyword matching
stop_words = {
    "a", "an", "the", "is", "are", "they",
    "their", "that", "with", "and", "or",
    "in", "on", "of", "to", "for", "about",
    "someone", "something", "two", "have",
    "been", "by", "as", "it", "who", "after"
}

# Make sure the database contains movies
if collection.count() == 0:
    print("No movies found in the database!")

else:
    # Run each test query separately
    for query in test_queries:
        print("\n" + "=" * 50)
        print("QUERY:", query)

        # Search ChromaDB using semantic similarity
        results = collection.query(
            query_texts=[query],
            n_results=min(10, collection.count())
        )

        # Extract important words from the query
        query_words = set(
            re.findall(r"[a-z]+", query.lower())
        )

        important_words = query_words - stop_words

        # Go through the search results
        for i in range(len(results["ids"][0])):
            title = results["metadatas"][0][i]["title"]
            summary = results["documents"][0][i]
            distance = results["distances"][0][i]

            print(f"\n{i + 1}. {title}")
            print("Distance:", round(distance, 4))
            print("Summary:", summary[:400])

            # Extract words from the full movie summary
            summary_words = set(
                re.findall(r"[a-z]+", summary.lower())
            )

            # Find words shared by the query and summary
            found_words = important_words & summary_words

            print("Keyword overlap:", sorted(found_words))

    print("\nSemantic search testing complete!")
