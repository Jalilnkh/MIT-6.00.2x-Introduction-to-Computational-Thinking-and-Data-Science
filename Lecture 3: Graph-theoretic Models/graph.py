
class Node():
    def __init__(self, name=None) -> None:
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self) -> str:
        return self.name 


class DiGraph:
    def __init__(self) -> None:
        self.edges = {}
    
    def add_node(self, node):
        if node in self.edges:
            raise ValueError('Duplicate Nodes')
        else:
            self.edges[node] = []
        
    def add_edges(self, edge):
        src = edge.get_source()
        dst = edge.get_destination()
        if not (src in self.edges and dst in self.edges):
            raise ValueError('Node not in Graph')
        self.edges[src].append(dst)

    def children(self, node):
        return self.edges[node]
    
    def has_node(self, node):
        return node in self.edges
    
    def get_node(self, name):
        for n in self.edges:
            if n.get_name() == name:
                return n
        raise NameError(name)
    
    def __str__(self) -> str:
        result = ''
        for src in self.edges:
            for dst in self.edges[src]:
                result = result + src.get_name() + '->'\
                    + dst.get_name() + '\n'
        
        return result[:-1]

class Edge():
    def __init__(self, src, dst) -> None:
        self.src = src
        self.dst = dst
    
    def get_source(self):
        return self.src
    
    def get_destination(self):
        return self.dst
    
    def __str__(self) -> str:
        return self.src.get_name() + '->' + self.dst.get_name()
     

# Example

def build_city_graph(graph_type):
    g = graph_type()
    for node in ('Ardabil','Sarab', 'Tabriz', 'Xoi', 'Urmia', 'Sulduz', 'Savic Bulag'):
        g.add_node(Node(node))
    g.add_edges(Edge(g.get_node('Ardabil'), g.get_node('Sarab')))
    g.add_edges(Edge(g.get_node('Sarab'), g.get_node('Tabriz')))
    g.add_edges(Edge(g.get_node('Tabriz'), g.get_node('Xoi')))
    g.add_edges(Edge(g.get_node('Xoi'), g.get_node('Urmia')))
    g.add_edges(Edge(g.get_node('Sulduz'), g.get_node('Urmia')))
    g.add_edges(Edge(g.get_node('Urmia'), g.get_node('Savic Bulag')))
    g.add_edges(Edge(g.get_node('Sulduz'), g.get_node('Savic Bulag')))

    return g

    
    
    
