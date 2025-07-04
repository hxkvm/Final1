class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self.heap.sort()

    def extract_min(self):
        return self.heap.pop(0)


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = MinHeap()
    heap.insert((0, start))

    while heap.heap:
        current_distance, current_node = heap.extract_min()

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heap.insert((distance, neighbor))

    return distances
