def compute_average_imdb_score_by_category(movie_list, category):
    imdb_scores = [movie['imdb_score'] for movie in movie_list if 'category' in movie and 'imdb_score' in movie
                   and movie['category'].lower() == category.lower() and isinstance(movie['imdb_score'], (int, float))]
    
    if not imdb_scores:
        return None

    average_score = sum(imdb_scores) / len(imdb_scores)
    return average_score