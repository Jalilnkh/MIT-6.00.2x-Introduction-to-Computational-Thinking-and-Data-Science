

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
    
    def has_node(self, name):
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


class Node():
    def __init__(self, name=None) -> None:
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self) -> str:
        return self.name 
    

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
        
