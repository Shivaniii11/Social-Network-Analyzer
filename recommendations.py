def recommend_connections(graph, user):
    direct = set(graph.get(user, []))
    rec = {}

    for friend in direct:
        for foaf in graph.get(friend, []):
            if foaf != user and foaf not in direct:
                rec[foaf] = rec.get(foaf, 0) + 1

    return sorted(rec.items(), key=lambda x: x[1], reverse=True)