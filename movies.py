import random

class Movie:
    def __init__(self, title, plot, description, actors, rating):
        self.title = title
        self.plot = plot
        self.description = description
        self.actors = actors
        self.rating = rating

# List of random movies
movies = []

# Generate a random list of 50 movies
for _ in range(50):
    title = "Movie " + str(random.randint(1, 1000))
    plot = "Plot of " + title
    description = "Description of " + title
    actors = [f"Actor-{i}" for i in range(1, random.randint(2, 6))]
    rating = round(random.uniform(1, 5), 2)
    movie = Movie(title, plot, description, actors, rating)
    movies.append(movie)

# Print the randomly generated movie details
# for movie in movies:
#     print(f"Title: {movie.title}")
#     print(f"Plot: {movie.plot}")
#     print(f"Description: {movie.description}")
#     print(f"Actors: {', '.join(movie.actors)}")
#     print(f"Rating: {movie.rating}")
#     print()