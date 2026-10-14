def boolean_search(query, index):
    results = set()
    for clause in query.lower().split():
        terms = [t for t in clause.split("&") if t]
        if not terms:
            continue
        docs = set(index.get(terms[0], []))
        for term in terms[1:]:
            docs &= set(index.get(term, []))
        results |= docs
    return sorted(results)
