from collections import deque

def build_graph(connections):
    graph = {}
    for u, v in connections:
        graph.setdefault(u, []).append(v)
    return graph


def mutual_connections(graph, u1, u2):
    return list(set(graph.get(u1, [])) & set(graph.get(u2, [])))


def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                queue.append((neighbor, path + [neighbor]))

    return None


def most_connected(graph):
    return max(graph.items(), key=lambda x: len(x[1]))