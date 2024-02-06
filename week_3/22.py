def get_movies_by_category(movie_list, category):
    movies_in_category = [movie for movie in movie_list if 'category' in movie and movie['category'].lower() == category.lower()]
    return movies_in_category