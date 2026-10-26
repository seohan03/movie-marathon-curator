# movie-marathon-curator

## Project Overview
A semantic movie recommendation and marathon planning application that recommends movies based on a user's desired mood or storyline. The application also allows users to create a personalized movie marathon by choosing different moods for the beginning, middle, and end. I chose this idea because of my own interest in movies and because movie recommendations based on feelings/themes can be difficult to find through traditional keyword searches.

## Dataset and Database
Dataset: CMU Movie Summary Corpus

I didn't use all 42,000+ movies for my project. A subset of 600 is enough to demonstrate semantic searching over a reasonably large collection. 

One item = one movie
Searchable text = movie's plot summary
Identifying info = movie's title

Each movie's full plot summary is one document rather than splitting it into smaller paragraphs. I did this because I wanted to recommend movies based on their overall story not just individual scenes. 

Movie title is stored as metadata because when ChromaDB finds a relavant plot summary, the program needs to know which movie that summary belongs to so it can display its title. 

The movie data is saved on my computer rather than existing only while the program is running which means that closing and reopening Python doesn't erase the database. (Verified through persistence test).

## How users use application
### Feature 1: Searching for a Movie
User selects search option and types a description of a movie they want. Example, "I want something emotional about someone returning to their hometown and remembering their past." The program would use collection.query() to find the 5 most semantically similar movies.

### Feature 2: Adding a New Movie
The user selects the "add movie" option and enters a movie title and plot summary. The program assigns the movie a unique ID and saves it to the existing ChromaDB collection.

Newly added movies can be searched immediately without rebuilding the entire database.

### Feature 3: Creating a Movie Marathon
The user describes three diferent moods where you can input a beginning, middle, and end mood. The program searches for movies corresponding to each mood and puts them into a viewing order. 

I made sure that the same movie wouldn't be recommended multiple time and considered how different each film would be using cosine similarity and a variety penalty. I also display the plot information and similarity details to help explain to the users the choices that the program made. 

## Semantic Search vs. Keyword Search
### Example 1: Nostalgia and returning to the past

Exact text query: "A reflective story about someone yearning to relive the happiness of their younger days."

Movie Retrieved: Chandrolsavam (Ranked #4 in semantic search)

The user asks for a movie about someone wanting to experience the happiness of their youth again. Chandrolsavam describes a man returning to his hometown and trying to recapture moments from his past.

Why keyword search would fail: The only reported keyword overlap was the generic word "story." A keyword search that would rely on important words like "yearning," "relive," and "younger" would miss the connection because the movie summary instead describes concepts such as nostalgia and revisiting the past.

### Example 2: Friendship between people with different personalities

Exact text query: "Two adolescents with contrasting temperaments build a lasting bond amid social exclusion."

Movie Retrieved: Mina Tannenbaum (Ranked #2 in semantic search and no keyword search comparison overlap)

Follows two girls who feel like outsiders and become friends despite having little in common. 

Why keyword search would fail: The movie had no matching keywords in the tested comparison, giving it a keyword score of zero. A traditional keyword search would miss the connection between "contrasting temperaments" and having different personalities, or "social exclusion" and feeling like outsiders. However, ChromaDB was able to recognize these similar meanings and retrieve the movie.