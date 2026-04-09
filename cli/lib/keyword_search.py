import string

from lib.search_utils import SEARCH_LIMIT, load_movies


def search(query: str, limit: int = SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    for movie in movies:
        preprocess_query = preprocess_text(query)
        preprocess_title = preprocess_text(movie["title"])
        if preprocess_query in preprocess_title:
            results.append(movie)
            if len(results) >= limit:
                break
    return results


def preprocess_text(text: str) -> str:
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text
