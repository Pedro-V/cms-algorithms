# Grafo direcionado/
class Vertex:
    def __init__(self, val) -> None:
        self.value = val
        self.adjacent_vertices = []
    
    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)

# Depth First
def dfs_traverse(vertex, visited_vertices={}):
    visited_vertices[vertex.value] = True
    for adjacent_vertex in vertex.adjacent_vertices:
        if visited_vertices[adjacent_vertex.value]:
            continue
        dfs_traverse(adjacent_vertex, visited_vertices)

def dfs(vertex, search_value, visited_vertices={}):
    if vertex.value == search_value:
        return
    visited_vertices[vertex.value] = True
    for adj_vertex in vertex.adjacent_vertices:
        if visited_vertices[adj_vertex.value]:
            continue
        vertex_were_searching_for = dfs(adj_vertex, search_value, visited_vertices)
        if vertex_were_searching_for:
            return vertex_were_searching_for
    return None

# Breadth-First
def bfs_traverse(vertex, visited_vertices={}):
    visited_vertices[vertex.value] = True
    queue = [vertex]
    # enquanto a queue não estiver vazia
    while queue:
        # retire da queue o último (current)
        current_vertex = queue.pop()
        # itere sobre os adjacente do current
        for adj_vertex in current_vertex:
            if visited_vertices[adj_vertex.value]:
                continue
            visited_vertices[adj_vertex.value] = True
            queue.append(adj_vertex)
    
def bfs(vertex, searched_value, visited_vertices={}):
    visited_vertices[vertex.value] = True
    queue = [vertex]
    while queue:
        current_vertex = queue.pop()
        if current_vertex.value == searched_value:
            return
        for adj_vertex in current_vertex:
            if visited_vertices[adj_vertex.value]:
                continue
            visited_vertices[adj_vertex.value] = True
            queue.append(adj_vertex)
    return None

# WEIGHTED GRAPHS
class WeightedGraphVertex:
    def __init__(self, val) -> None:
        self.value = val
        self.adjacent_vertices = {}
    def add_adjacent_vertex(self, vertex, weight):
        self.adjacent_vertices[vertex] = weight

# Algoritmo de Djikstra

def dijkstra_shortest_path(starting_city:WeightedGraphVertex, final_destination):
    cheapest_prices_table = {}
    cheapest_previous_stopover_city_table = {}

    unvisited_cities = []
    visited_cities = {}

    # custo zero de chegar à cidade inicial
    cheapest_prices_table[starting_city.value] = 0
    current_city = starting_city

    while current_city:
        visited_cities[current_city.value] = True
        # Remover todas as instancias de uma dada cidade
        unvisited_cities = [city for city in unvisited_cities if city != current_city]

        # checamos e iteramos sobre as cidades adjacentes da cidade atual
        for adjacent_city, price in current_city.adjacent_vertices.items():
            # Caso a cidade não tenha sido visitada
            if not visited_cities[adjacent_city.value]:
                unvisited_cities.append(adjacent_city)

            price_through_current_city = cheapest_prices_table[current_city.value] + price
            if not cheapest_prices_table.get(adjacent_city.value) or (price_through_current_city < cheapest_prices_table[adjacent_city.value]):
                cheapest_prices_table[adjacent_city.value] = price_through_current_city
                cheapest_previous_stopover_city_table[adjacent_city.value] = current_city.value

        # o valor da cidade atual será atualizado para ser a cidade cujo preço vindo da cidade original é o menor
        current_city = unvisited_cities[0]
        for unv_city in unvisited_cities[1:]:
            if cheapest_prices_table[unv_city.value] < cheapest_prices_table[current_city.value]:
                current_city = unv_city

    shortest_path = []
    current_city_name = final_destination.value
    while current_city_name != starting_city.value:
        shortest_path.append(current_city_name)
        current_city_name = cheapest_previous_stopover_city_table[current_city_name]
    
    shortest_path.append(starting_city.value)
    shortest_path.reverse()
    return shortest_path


# EXERCICIOS
# Q1
# nails polihs, pins, needles e hammer

# Q2: o final de cada linha retorna ao A
# A -> B -> E -> J -> F
#                |-> O
# A -> C -> G -> K
# A -> D -> I -> M -> H -> L
#           |-> N -> P


# Q3: 
# A -> B -> C -> D -> E -> F -> J -> O
# -> G -> K -> I -> H -> M -> N -> L -> P

# Q4: Ja feito:
print(bfs)
# Q5