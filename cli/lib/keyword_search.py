import string

from lib.search_utils import SEARCH_LIMIT, load_movies


def search(query: str, limit: int = SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    query_tokens = preprocess_text(query)

    for movie in movies:
        title_tokens = preprocess_text(movie["title"])

        if has_matching_token(query_tokens, title_tokens):
            results.append(movie)

            if len(results) >= limit:
                break

    return results


def preprocess_text(text: str) -> list[str]:
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()


def has_matching_token(query_tokens: list[str], title_tokens: list[str]) -> bool:
    for query in query_tokens:
        for title in title_tokens:
            if query in title:
                return True
    return False
