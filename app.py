from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from movies import movies


class Movie:
    def __init__(self, title, plot, description, actors, rating):
        self.title = title
        self.plot = plot
        self.description = description
        self.actors = actors
        self.rating = rating

#recommend movies based on user's watched movie
def recommend_movies(watched_movie, movie_list):
    #TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    #calculate TF-IDF vectors for each movie
    corpus = [watched_movie.plot] + [movie.plot for movie in movie_list]
    tfidf_matrix = vectorizer.fit_transform(corpus)

    #Calculating cosine similarity between watched movie and all other movies
    similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix)[0][1:]

    #Sorting movies based on similarity
    recommended_movies_indices = similarities.argsort()[::-1]

    return [movie_list[i] for i in recommended_movies_indices]


movies = movies


#user interaction
watched_movie = movies[0]

#recommending similar movies
recommended_movies = recommend_movies(watched_movie, movies)

print("Watched movie: ",watched_movie)


count = 0
# Printing recommended movies
print('Recommended movies:')
for movie in recommended_movies:
    print(f'- {movie.title} (Rating: {movie.rating})')
    count += 1
    if count == 10:
        break


