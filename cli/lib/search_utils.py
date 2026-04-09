import json
import os

SEARCH_LIMIT = 5
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")
STOPWORDS_PATH = os.path.join(PROJECT_ROOT, "data", "stopwords.txt")


def load_movies() -> list[dict]:
    with open(DATA_PATH, "r") as file:
        data = json.load(file)
    return data["movies"]


def load_stop_words() -> set[str]:
    with open(STOPWORDS_PATH, "r") as file:
        return set(file.read().splitlines())
