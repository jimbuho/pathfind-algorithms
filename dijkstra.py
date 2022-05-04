import sys
import graphs
import random

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    # Usaremos este diccionario para almacenar el costo de visitar cada nodo
    # y lo actualizamos mientras nos movemos alrededor del grafo
    shortest_path = {}
 
    # Usaremos este diccionario para almacenar la ruta mas corta conocida a un nodo distante
    previous_nodes = {}
 
    # Usaremos max_value para inicializar un valor "infinito" de nodos no visitados 
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value

    # Sin embargo, inicializamos el nodo inicial con 0 
    shortest_path[start_node] = 0
    
    # El algoritmo se ejecuta hasta que visitemos todos los nodos
    while unvisited_nodes:
        # El siguiente segmento de codigo permite encontrar al nodo
        # con el menor score
        current_min_node = None
        for node in unvisited_nodes: # Iteramos los nodos
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # El siguiente bloque de codigo recupera los nodos vecinos del nodo 
        # actual y actualiza sus distancias
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # Tambien actualizamos la mejor ruta hacia el nodo actual
                previous_nodes[neighbor] = current_min_node
 
        # Luego de visitar sus vecinos, marcamos al nodo como "visitado"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print("Encontramos la ruta mas corta a un costo total de {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


def generate_random_graph(nodes):
    random_graph = {}

    print(nodes)
    
    for node in nodes:
        random_graph[node] = {}

        new_list = nodes.copy()
        new_list.remove(node)

        for i in range(1, random.choice(range(1, len(new_list)))):
            random_node = random.choice(new_list)
            random_graph[node][random_node] = random.choice(range(1, 10))

    return random_graph

nodes = ["Quito", "Ibarra", "Cuenca", 
"Loja", "Santo Domingo", "Esmeraldas", 
"Ambato", "Guayaquil"]

def main():
    args = sys.argv[1:]

    start = nodes[0]
    target = nodes[1]
    if len(args) == 1:
        start = args[0]
        if start not in nodes:
            print("Start Node", start, "not in", nodes)
            return
    elif len(args) == 2:
        target = args[1]
        if target not in nodes:
            print("Target Node", target, "not in", nodes)
            return
    
    init_graph = generate_random_graph(nodes)
    graph = graphs.Graph(nodes, init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start)
    print_result(previous_nodes, shortest_path, start_node=start, target_node=target)

if __name__ == "__main__":
    main()