import json
import random
from pathlib import Path

# Location of our dataset
data_folder = Path("data/MovieSummaries")

# STEP 1: Load movie titles
movie_titles = {}

with open(data_folder / "movie.metadata.tsv",
          "r", encoding="utf-8") as file:

    for line in file:
        columns = line.strip().split("\t")

        if len(columns) >= 3:
            movie_id = columns[0]
            title = columns[2]

            movie_titles[movie_id] = title

print("Movie titles loaded:", len(movie_titles))



# STEP 2: Match and filter movies
movies = []

with open(data_folder / "plot_summaries.txt",
          "r", encoding="utf-8") as file:

    for line in file:
        parts = line.strip().split("\t", 1)

        if len(parts) != 2:
            continue

        movie_id, summary = parts

        # Only keep movies with titles and detailed summaries
        if movie_id in movie_titles and len(summary.split()) >= 80:
            movie = {
                "id": movie_id,
                "title": movie_titles[movie_id],
                "summary": summary
            }

            movies.append(movie)

print("Usable movies:", len(movies))

# STEP 3: Select 600 movies

if len(movies) < 600:
    raise ValueError("Not enough usable movies!")

random.seed(113)

selected_movies = random.sample(movies, 600)

print("Selected movies:", len(selected_movies))


# STEP 4: Save movies to a JSONL file

output_path = Path("data/movies_600.jsonl")

with open(output_path, "w", encoding="utf-8") as file:
    for movie in selected_movies:
        file.write(json.dumps(movie, ensure_ascii=False) + "\n")

print("Saved movies to:", output_path)

# Display 3 sample movies
for movie in selected_movies[:3]:
    print("\nTitle:", movie["title"])
    print("Summary:", movie["summary"][:150])
