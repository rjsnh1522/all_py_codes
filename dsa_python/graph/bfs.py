from queue import Queue

adj_list = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A", "E", "F"],
    "E": ["D", "F", "G"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["G", "F"]
}


def bfs_code(adj_list):
    visited = {}
    level = {}
    parent = {}
    bfs_traversal_output = []
    queue = Queue()

    for node in adj_list.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1

    source = "A"
    visited[source] = True
    level[source] = 0
    queue.put(source)

    while not queue.empty():
        u = queue.get()
        bfs_traversal_output.append(u)

        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u]+1
                queue.put(v)

    print(bfs_traversal_output)
    print(level)


print(bfs_code(adj_list))
