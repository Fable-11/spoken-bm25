import json
import time

from core.bool_search import boolean_search
from core.invert_idx import create_index


def load_news(path):
    corpus = []
    with open(path) as file:
        for line in file:
            if line.strip():
                article = json.loads(line)
                corpus.append(f"{article['headline']} {article['short_description']}")
    return corpus


corpus = load_news("data/news.json")
print(f"Loaded {len(corpus)} articles")

start = time.time()
index = create_index(corpus)
end = time.time()
print(f"Built index with {len(index)} terms in {(end - start) * 10**6:.0f} us\n")

# space = OR, & = AND
queries = [
    "oil&prices",
    "climate&change",
    "movies",
    "samsung&sony tv",
    "apple&iphone macbook",
]

print(f"{'Query':<20}{'Results':>10}{'Time (us)':>14}")
for query in queries:
    start = time.time()
    results = boolean_search(query, index)
    end = time.time()
    print(f"{query:<20}{len(results):>10}{(end - start) * 10**6:>14.0f}")
