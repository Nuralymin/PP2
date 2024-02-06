def is_good_movie(movie):
    # Assuming the movie dictionary has a key 'imdb_score' for the IMDB score
    if 'imdb_score' in movie and isinstance(movie['imdb_score'], (int, float)):
        return movie['imdb_score'] > 5.5
    else:
        # If 'imdb_score' is not present or not a valid number, consider it not a good movie
        return False