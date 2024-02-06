def compute_average_imdb_score(movie_list):
    imdb_scores = [movie['imdb_score'] for movie in movie_list if 'imdb_score' in movie and isinstance(movie['imdb_score'], (int, float))]
    
    if not imdb_scores:
        return None  # Return None if no valid IMDB scores are found

    average_score = sum(imdb_scores) / len(imdb_scores)
    return average_score