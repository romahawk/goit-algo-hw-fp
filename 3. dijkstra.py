import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append((to_node, weight))

def dijkstra(graph, start_node):
    # Відстань від початкової вершини до себе дорівнює 0
    distances = {node: float('infinity') for node in graph.edges}
    distances[start_node] = 0

    # Пріоритетна черга для вибору вершини з найменшою відстанню
    priority_queue = [(0, start_node)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Пропустити обробку, якщо ми знайшли кращий шлях
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges.get(current_node, []):
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад використання
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)

    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)

    print(f"Найкоротші шляхи від вершини {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"Відстань до {node}: {distance}")
