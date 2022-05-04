from pyvis.network import Network
import networkx as nx
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

        self.draw = GraphDrawer(len(init_graph.items()))
        self.draw.draw_graph(self.graph)
        self.draw.show_all()
        
    def construct_graph(self, nodes, init_graph):
        '''
        Construye un grafo completo y simetrico
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        return self.graph[node1][node2]

class GraphDrawer:

    def __init__(self, max_nodes):
        self.nx_graph = nx.Graph()

    def add_node(self, id, title, size=15, group=1):
        self.nx_graph.add_node(id, size=size, title=title, group=group)

    def add_edge(self, source_id, target_id, weight):
        self.nx_graph.add_edge(source_id, target_id, weight=weight)

    def draw_graph(self, graph):
        """
        Dibuja un grafo que puede tener una estructura como la del ejemplo:

        [('Reykjavik', {'Oslo': 5, 'London': 4}), 
        ('Oslo', {'Berlin': 1, 'Moscow': 3, 'Reykjavik': 5}), 
        ...]

        """
        
        for k in graph.keys():
            self.add_node(k[0], k)

        for node, edges in graph.items():
            for k,v in edges.items():
                self.add_edge(node[0], k[0], v)

    def show_all(self):
        nt = Network('500px', '500px')
        nt.from_nx(self.nx_graph)
        nt.show('nx.html')
