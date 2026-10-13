import networkx as nx

# Check readme.md for details on each sub-task

def calculate_node_degrees(edges: list) -> dict:
    """
    Sub-task 1: Calculate the degree of each node in an undirected graph.

    Args:
        edges: List of tuples representing edges, e.g. [('A', 'B'), ('B', 'C')]

    Returns:
        Dictionary mapping each node to its degree.
    """
    degrees = {}

    for u, v in edges:
        degrees[u] = degrees.get(u, 0) + 1
        degrees[v] = degrees.get(v, 0) + 1

    return degrees

pass

from collections import deque

def find_shortest_path(edges: list, source: str, target: str) -> list:
    """Sub-task 2: Find the shortest path between source and target nodes."""

    # Build adjacency list
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    # BFS
    queue = deque([(source, [source])])
    visited = {source}

    while queue:
        node, path = queue.popleft()

        if node == target:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []

def count_connected_components(edges: list) -> int:
    """
    Sub-task 3: Count the number of connected components
    in an undirected graph.
    """

    # Build adjacency list
    graph = {}

    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    visited = set()
    components = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph :
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            components += 1
            dfs(node)

    return components
pass

from collections import deque

def compute_topological_sort(directed_edges: list) -> list:
    """Sub-task 4 – Topological Sort in a Directed Acyclic Graph (DAG)"""
    graph = {}
    in_degree = {}
    nodes = set()

    # Build graph
    for u, v in directed_edges:
        nodes.add(u)
        nodes.add(v)

        if u not in graph:
            graph[u] = []
        graph[u].append(v)

        in_degree[v] = in_degree.get(v, 0) + 1

        if u not in in_degree:
            in_degree[u] = 0

    # Queue of nodes with no incoming edges
    queue = deque()

    for node in nodes:
        if in_degree[node] == 0:
            queue.append(node)

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result
pass

def compute_average_clustering(edges: list) -> float:
    """Sub-task 5 – Average Clustering Coefficient"""
    # Build adjacency list
    graph = {}

    for u, v in edges:
        graph.setdefault(u, set()).add(v)
        graph.setdefault(v, set()).add(u)

    if not graph:
        return 0.0

    clustering_sum = 0.0

    for node in graph:
        neighbors = graph[node]
        k = len(neighbors)

        if k < 2:
            clustering_sum += 0.0
            continue

        # Count edges between neighbors
        links = 0
        neighbors_list = list(neighbors)

        for i in range(len(neighbors_list)):
            for j in range(i + 1, len(neighbors_list)):
                if neighbors_list[j] in graph[neighbors_list[i]]:
                    links += 1

        possible_links = k * (k - 1) / 2
        clustering_sum += links / possible_links

    return clustering_sum / len(graph)
pass

def main():
    print("Sub-task 1:", calculate_node_degrees([("A", "B"), ("B", "C"), ("B", "D")]))
    print("Sub-task 2:", find_shortest_path([("A", "B"), ("B", "C"), ("A", "C"), ("C", "D")], "A", "D"))
    print("Sub-task 3:", count_connected_components([("A", "B"), ("B", "C"), ("D", "E")]))
    print("Sub-task 4:", compute_topological_sort([("A", "B"), ("B", "C")]))
    print("Sub-task 5:", compute_average_clustering([("A", "B"), ("B", "C"), ("C", "A")]))

if __name__ == "__main__":
    main()
