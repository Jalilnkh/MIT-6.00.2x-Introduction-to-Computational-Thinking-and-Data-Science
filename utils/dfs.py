


def dfs(graph, start, end, path, shortest, to_print=False):
    path = path + [start]
    if to_print:
        print(f'Current DFS path: {print_path(path)}')
    if start == end:
        return path
    for node in graph.children(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                new_path = dfs(graph, node, end, path, shortest, to_print)
            if new_path != None:
                shortest = new_path
        elif to_print:
            print("Already existed", node)
    return shortest

def short_path(graph, start, end, to_print=False):
    return dfs(graph, start, end, [], None, to_print)


def print_path(path):
    """
    Prints the path in a readable format.

    Args:
    path (list): A list of nodes representing the path.

    Returns:
    str: A string representation of the path.
    """
    return ' -> '.join([str(node) for node in path])