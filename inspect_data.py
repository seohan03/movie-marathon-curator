from pathlib import Path

# Find the movie summaries file
file_path = Path("data/MovieSummaries/plot_summaries.txt")

movie_count = 0

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split("\t", 1)

        if len(parts) == 2:
            movie_id, summary = parts

            movie_count += 1

            # Show the first 3 movie summaries
            if movie_count <= 3:
                print("Movie ID:", movie_id)
                print("Summary:", summary[:200])
                print("--------------------------")

print("Total movies:", movie_count)
