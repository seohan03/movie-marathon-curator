AI Prompt Log
Purpose: I used ChatGPT to help brainstorm my project, learn ChromaDB, implement semantic search, debug my code, and test the recommendation system. AI was used to generate initial code, then I ran and evaluated the functions myself, including checking whether the movie recommendations actually made sense.

## 1. Project Brainstorming & Prompt Planning
Prompt: im interested in building something related to movies for my vector database assignment i want users to be able to describe a specific mood or vibe they're looking for rather than searching for movies by genre or title. help me develop this into a more concrete project idea and write a detailed prompt i can use to start a new coding conversation. i want to use python and chromaDB. users should be able to describe a movie based on its mood instead of having to search for it by title/genre. 

Response: ChatGPT suggested creating a Movie Marathon Curator that uses semantic search to recommend movies based on moods, themes, and story descriptions. It helped me develop the idea into a more detailed project prompt for building the application with Python and ChromaDB.

## 2. Setting up ChromaDB
Prompt: i want the movie data to be stored locally and remain saved after i close the program. explain how persistent storage works and give me the code to initialize the database

Response: ChatGPT explained how ChromaDB stores data locally and provided code using chromadb.PersistentClient(path="./chroma_db") to create a persistent database. It also explained how get_or_create_collection() allows the program to access the same movie collection across different sessions.


## 3. Loading the Dataset
Prompt: use this cmu movie summary corpus help me write a python script that reads the dataset and selects around 600 movie summaries and stores them in chromaDB with their titles and plot summaries. how can i prevent duplicate entries when running the script again

Response: ChatGPT helped write a Python script to load approximately 600 movie summaries from the CMU Movie Summary Corpus into ChromaDB. It explained how movie summaries are converted into embeddings and how unique IDs can prevent duplicate entries when loading the dataset multiple times.


## 4. Implementing Semantic Search
Prompt: now that i have movie summaries stored in chromaDB, help me implement semantic search. i want users to type a natural language description of a movie they're looking for and receive the five most relevant recommendations. each recommendation should show the title and part of the plot summary

Response: ChatGPT provided a search function using ChromaDB's collection.query() method to retrieve the five most semantically similar movies based on a user's natural-language input. The function displays each movie's title and a shortened plot summary so users can understand the recommendations.

## 5. Adding New Movies
Prompt: i want users to be able to add their own movies while the program is running how do i implement a function that asks for a movie title and plot summary and stores the movie in chromaDB and makes it immediately available in semantic search. explain how to assign a unique ID to each movie

Response: ChatGPT helped implement a function that asks users to enter a movie title and plot summary through the terminal. It used unique IDs to store each new movie in ChromaDB and explained how the newly added movies could be retrieved immediately through semantic search without restarting the program.


## 6. Creating Personalized Movie Marathons
Prompt: i want to make this app more useful than a basic movie search engine implement a feature where users enter 3 different moods like the beginning, middle, and ending of a movie marathon. the program should use semantic search to select three different movies that fit those moods and display them in order

Response: ChatGPT helped create a create_marathon() function that asks users to describe three moods for the beginning, middle, and ending of their movie marathon. The function searches ChromaDB for movies matching each mood and selects three different films to create a personalized viewing order.



## 7. Testing Semantic Search
Prompt: help me create a python test script that runs queries and displays the top 10 retrieved movies and their distances and checks for any overlapping keywords. i should be able to evaluate the results myself rather than assume every recommendation is correct

Response: ChatGPT helped create test_semantic.py to run natural-language queries and display the top ten matching movies, their similarity distances, and keyword overlap. After testing different queries, I identified Mina Tannenbaum and Chandrolsavam as relevant results that were retrieved despite having no important keyword overlap with the queries.

## 8. Comparing with Keyword Search
Prompt: compare my chromadb result against a basic keyword search. i want to write a separate python script that ranks movies based on matching words in their plot summaries. test whether semantic search finds relavant movies that keyword search misses

Response: ChatGPT helped write keyword_baseline.py to compare semantic search against a basic keyword-matching approach. The script checks whether important words from a query appear in movie summaries. Testing showed that Mina Tannenbaum could be retrieved through semantic search despite having zero keyword matches in the baseline. The comparison for Chandrolsavam still needed verification.

## 9. Testing Database Persistence
Prompt: help me create a test that adds a movie, confirms it is searchable and closes and reopens the database and checks whether the movie still exists

Response: ChatGPT provided instructions for testing whether newly added movies remained searchable after closing and reopening the application. It also helped create verify_persistence.py, which reconnects to the ChromaDB collection and checks whether a previously inserted movie still exists using its title.

## 10. Improving Marathon Recommendations
Prompt: my marathon generator right now selects movies based on how semantically similar they are but i want to have the recommendations feel more intentional so help me improve the selection algorithm so it avoids suggesting the same movie and considers variety of the three recommended films and i want it to explain why each movie matches its request mood. keep the code simple enough for me to understand.

Response: ChatGPT improved the create_marathon() function by adding duplicate prevention and a variety penalty based on cosine similarity between movie embeddings. The updated algorithm considers both how closely a movie matches the requested mood and how similar it is to the other selected films. It also displays plot excerpts and similarity information to help explain the recommendations.

## 11. Testing and Debugging
Prompt: i have separate functions for searching movies, adding movies, and creating marathons i need them to work together in one command line. help me make a menu that lets users select these features and exit the program and identify any errors and test each option without rewriting parts of the code that already work.

Response: ChatGPT provided an integrated main.py application with a command-line menu for searching movies, adding movies, creating personalized marathons, and exiting. It gave me test inputs for each feature and instructions for checking that newly added movies were immediately searchable and remained saved after restarting the program.