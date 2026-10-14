import re

def create_index(corpus):
    index = {}
    for doc_id, doc in enumerate(corpus):
        for term in set(re.findall(r"\w+", doc.lower())):
            index.setdefault(term, []).append(doc_id)
    return index
