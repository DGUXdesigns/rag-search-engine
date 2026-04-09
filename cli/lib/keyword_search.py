import string

from lib.search_utils import SEARCH_LIMIT, load_movies, load_stop_words

STOP_WORDS = load_stop_words()


def search(query: str, limit: int = SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    query_tokens = tokenize_text(query)

    for movie in movies:
        title_tokens = tokenize_text(movie["title"])

        if has_matching_token(query_tokens, title_tokens):
            results.append(movie)

            if len(results) >= limit:
                break

    return results


def preprocess_text(text: str) -> str:
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


def tokenize_text(text: str) -> list[str]:
    text = preprocess_text(text)
    tokens = text.split()
    tokens = remove_stopwords(tokens, STOP_WORDS)
    return tokens


def has_matching_token(query_tokens: list[str], title_tokens: list[str]) -> bool:
    for query in query_tokens:
        for title in title_tokens:
            if query in title:
                return True
    return False


def remove_stopwords(tokens: list[str], stopwords: set[str]) -> list[str]:
    return [word for word in tokens if word not in stopwords]
