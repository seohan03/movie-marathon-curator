
import chromadb
import uuid

# Connect to the persistent database
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="movies")


# OPTION 1: Search for movies
def search_movies():
    if collection.count() == 0:
        print("No movies in the database.")
        return

    query = input("\nDescribe the movie you want: ").strip()

    if not query:
        print("Please enter a description.")
        return

    results = collection.query(
        query_texts=[query],
        n_results=min(5, collection.count())
    )

    print("\n=== MOVIE RECOMMENDATIONS ===")

    for i in range(len(results["ids"][0])):
        title = results["metadatas"][0][i]["title"]
        summary = results["documents"][0][i]

        print(f"\n{i + 1}. {title}")
        print("Plot:", summary[:300])


# OPTION 2: Add a new movie
def add_movie():
    print("\n=== ADD A NEW MOVIE ===")

    title = input("Movie title: ").strip()
    summary = input("Plot summary: ").strip()

    if not title or not summary:
        print("Title and summary cannot be empty.")
        return

    # Generate a unique ID for the new movie
    movie_id = "user-" + str(uuid.uuid4())

    collection.add(
        ids=[movie_id],
        documents=[summary],
        metadatas=[{"title": title}]
    )

    print(f"\nSuccessfully added: {title}")
    print("This movie is now searchable!")


# OPTION 3: Create a movie marathon

def create_marathon():
    if collection.count() < 3:
        print("You need at least 3 movies!")
        return

    print("\n=== CREATE YOUR MOVIE MARATHON ===")

    beginning = input("Beginning mood: ").strip()
    middle = input("Middle mood: ").strip()
    ending = input("Ending mood: ").strip()

    if not beginning or not middle or not ending:
        print("Please enter all three moods.")
        return

    stages = [
        ("Beginning", beginning),
        ("Middle", middle),
        ("Ending", ending)
    ]

    used_ids = set()
    selected_vectors = []

    # Compare how similar two movie embeddings are
    def cosine_similarity(a, b):
        dot_product = sum(x * y for x, y in zip(a, b))
        length_a = sum(x * x for x in a) ** 0.5
        length_b = sum(y * y for y in b) ** 0.5

        if length_a == 0 or length_b == 0:
            return 0

        return dot_product / (length_a * length_b)

    print("\n=== YOUR PERSONALIZED MOVIE MARATHON ===")

    for stage, mood in stages:
        results = collection.query(
            query_texts=[mood],
            n_results=min(15, collection.count()),
            include=[
                "documents",
                "metadatas",
                "distances",
                "embeddings"
            ]
        )

        best_index = None
        best_score = float("inf")

        # Balance mood relevance with movie variety
        for i, movie_id in enumerate(results["ids"][0]):
            if movie_id in used_ids:
                continue

            distance = results["distances"][0][i]
            vector = results["embeddings"][0][i]

            variety_penalty = 0

            if selected_vectors:
                similarity = max(
                    cosine_similarity(vector, previous)
                    for previous in selected_vectors
                )

                variety_penalty = 0.15 * similarity

            score = distance + variety_penalty

            if score < best_score:
                best_score = score
                best_index = i

        if best_index is None:
            print(f"\n{stage}: No unique movie found.")
            continue

        i = best_index

        movie_id = results["ids"][0][i]
        title = results["metadatas"][0][i]["title"]
        summary = results["documents"][0][i]
        distance = results["distances"][0][i]
        vector = results["embeddings"][0][i]

        used_ids.add(movie_id)
        selected_vectors.append(vector)

        print(f"\n--- {stage.upper()} ---")
        print("Movie:", title)
        print("Requested mood:", mood)
        print("Plot:", summary[:350])

        print(
            "Why selected: Semantic match for this "
            "stage, balanced against repeated movies."
        )
        print("Semantic rank:", i + 1)
        print("Semantic distance:", round(distance, 4))

    print("\nEnjoy your movie marathon!")



# MAIN APPLICATION MENU
def main():
    while True:
        print("\n=== MOVIE MARATHON CURATOR ===")
        print("1. Search for movies")
        print("2. Add a new movie")
        print("3. Create a movie marathon")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            search_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            create_marathon()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
