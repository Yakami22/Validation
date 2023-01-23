from collections import deque

graph = {
   "a": ["b", "c"],
   "b": ["a", "d"],
   "c": ["a", "d"],
   "d": ["e"],
   "e": ["d"]
}

graph2 = {
    1: [2, 3],
    2: [5, 6],
    3: [],
    4: [4, 6],
    5: [4],
    6: [6]
}

graph3 = {
    0: [1, 3],
    1: [2],
    2: [0],
    3: [3, 4],
    4: [1, 5],
    5: [],
    6: []
}


def recursive_dfs(graph, node, visited=None):
    """
    Function to go through a graph recursively

    :param graph: the graph to use
    :param node: the node where we start
    :param visited: list of node visited initially null
    :return: list of node
    """

    if visited is None:
        visited = []

    if node not in visited:
        visited.append(node)

    unvisited = [n for n in graph[node] if n not in visited]

    for node in unvisited:
        recursive_dfs(graph, node, visited)

    return visited


def iterative_bfs(graph, start):
    """
    Iterative function for going through a graph

    :param graph: the graph to go through
    :param start: the node where to start
    :return: a list of all the nodes
    """
    visited = []
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            unvisited = [n for n in graph[node] if n not in visited]
            queue.extend(unvisited)

    return visited


print(recursive_dfs(graph3, 0))
