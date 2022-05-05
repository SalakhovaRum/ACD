import sys

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        '''Этот метод обеспечивает симметричность графика'''
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items(): #возвращает графы,которых еще не было
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        "Возвращает узлы графа"
        return self.nodes

    def get_outgoing_edges(self, node):
        "Возвращает соседей узла"
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Возвращает значение ребра между двумя узлами."
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node): #graph-это экземпляр класса; start_node-узел,с коорого мы начинаем посещения
    '''Инициализация списка непосещенных узлов:'''
    unvisited_nodes = list(graph.get_nodes())

    #Используем этот словарь,которая будет хранить каждое посещение по графах и обновлять их
    shortest_path = {}

    #Используем этот словарь,чтобы найти кратчайший путь
    previous_nodes = {}

    #Используем max_value для инициализации значения "бесконечности" непосещенных узлов
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    #Но мы показываем,что начальный узел == 0
    shortest_path[start_node] = 0

    #Алгоритм Дейкстры выполняется до тех пор, пока мы не посетим все узлы
    while unvisited_nodes:
        #Находим узел с наименьшей оценкой
        current_min_node = None
        for node in unvisited_nodes:  #Выполняется итерация по узлам
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        #Извлекаем соседей текущего узла и обновляем их расстояние
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                #Мы также обновляем наилучший путь к текущему узлу
                previous_nodes[neighbor] = current_min_node

        #После посещения "соседей", мы отмечаем,что посетили этот узел и удаляем его
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    #Добавить начальный узел вручную
    path.append(start_node)

    print("Найден следующий лучший маршрут с ценностью {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


nodes = ["Граф_1", "Граф_2", "Граф_3", "Граф_4", "Граф_5", "Граф_6", "Граф_7", "Граф_8"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["Граф_1"]["Граф_2"] = 17
init_graph["Граф_1"]["Граф_4"] = 5011
init_graph["Граф_2"]["Граф_6"] = 79
init_graph["Граф_2"]["Граф_3"] = 200
init_graph["Граф_3"]["Граф_7"] = 97
init_graph["Граф_3"]["Граф_8"] = 45555
init_graph["Граф_8"]["Граф_7"] = 10
init_graph["Граф_5"]["Граф_6"] = 2888
init_graph["Граф_5"]["Граф_8"] = 24
graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Граф_1")
print_result(previous_nodes, shortest_path, start_node="Граф_1", target_node="Граф_7")