"""Practice #59: breadth-first search (attempt 2)."""

from collections import deque


def build_graph(edges):
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    return graph


def bfs_distances(graph, start):
    """Breadth-first search: shortest hop count from start to every reachable node."""
    dist = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nxt in graph.get(node, []):
            if nxt not in dist:
                dist[nxt] = dist[node] + 1
                queue.append(nxt)
    return dist


if __name__ == "__main__":
    edges = [(0, 1), (0, 5), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5)]
    graph = build_graph(edges)
    start = edges[0][0]
    dist = bfs_distances(graph, start)
    print("distances from", start, ":", dist)
    assert dist[start] == 0
    assert all(abs(dist[a] - dist[b]) <= 1 for a, b in edges if a in dist)
