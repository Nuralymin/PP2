def get_good_movies(movie_list):
    good_movies = [movie for movie in movie_list if 'imdb_score' in movie and isinstance(movie['imdb_score'], (int, float)) and movie['imdb_score'] > 5.5]
    return good_movies