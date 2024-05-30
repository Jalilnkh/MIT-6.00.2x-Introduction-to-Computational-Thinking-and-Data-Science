from graph import build_city_graph, DiGraph
from utils.dfs import short_path, print_path
# Add utils directory to PYTHONPATH


def test_dfs(src: str, dst: str):
    graph = build_city_graph(DiGraph)
    shortest_path = short_path(
        graph, 
        graph.get_node(src), 
        graph.get_node(dst), 
        to_print=True)
    if shortest_path != None:
        print(f"The shortest path from {src} to {dst} is {print_path(shortest_path)}")


if __name__ == "__main__":
    test_dfs('Ardabil', 'Sulduz')