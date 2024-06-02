


def dfs(graph, start, end, to_print=False):
    init_path = [start]
    path_queue = [init_path]
    while len(path_queue) != 0:
        tmp_path = path_queue.pop(0)
        if to_print:
            print(f'Current BFS path: {print_path(tmp_path)}')
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path
        for node in graph.children(last_node):
            if node not in tmp_path:
                new_path = tmp_path + [node]
                path_queue.append(new_path)
    return None

def short_path(graph, start, end, to_print=False):
    return dfs(graph, start, end, to_print)


def print_path(path):
    """
    Prints the path in a readable format.

    Args:
    path (list): A list of nodes representing the path.

    Returns:
    str: A string representation of the path.
    """
    return ' -> '.join([str(node) for node in path])