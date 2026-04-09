from lib.search_utils import SEARCH_LIMIT, load_movies


def search(query: str, limit: int = SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    for movie in movies:
        if query in movie["title"].lower():
            results.append(movie)
            if len(results) >= limit:
                break
    return results
