
import chromadb

# Connect to our saved movie database
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="movies")


def find_movie(description, used_ids):
    # Find the 10 closest semantic matches
    results = collection.query(
        query_texts=[description],
        n_results=min(10, collection.count())
    )

    # Look through the recommended movies
    for i, movie_id in enumerate(results["ids"][0]):

        # Avoid recommending the same movie twice
        if movie_id not in used_ids:
            used_ids.add(movie_id)

            return {
                "title": results["metadatas"][0][i]["title"],
                "summary": results["documents"][0][i]
            }

    return None


def create_marathon():
    if collection.count() < 3:
        print("Add at least 3 movies first!")
        return

    print("\n=== CREATE YOUR MOVIE MARATHON ===")

    beginning = input("How should your marathon begin? ")
    middle = input("What should the middle feel like? ")
    ending = input("How should your marathon end? ")

    stages = [
        ("Beginning", beginning),
        ("Middle", middle),
        ("Ending", ending)
    ]

    used_ids = set()

    print("\n=== YOUR PERSONALIZED MARATHON ===")

    for stage, description in stages:
        movie = find_movie(description, used_ids)

        if movie:
            print(f"\n{stage}: {movie['title']}")
            print("Requested feeling:", description)
            print("Plot preview:", movie["summary"][:250])
        else:
            print(f"\n{stage}: No unique movie found")


if __name__ == "__main__":
    create_marathon()
