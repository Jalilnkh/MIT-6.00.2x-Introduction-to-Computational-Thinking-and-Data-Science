


def dfs(graph, start, end, path, shortest, to_print=False):
    path += [start]
    if to_print:
        print(f'Current DFS path: {print_path(path)}')
    if start == end:
        return path
    for node in graph.children(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                new_path = dfs(graph, start, end, path, shortest, to_print)
            if new_path != None:
                shortest = new_path
        elif to_print:
            print("Already existed", node)
    return shortest
