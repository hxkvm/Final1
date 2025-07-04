class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None  # If heap is empty, return None
        min_item = self.heap[0]
        # If there's only one element, pop it directly
        if len(self.heap) == 1:
            self.heap.pop()
        else:
            # Move the last item to the root and heapify down
            self.heap[0] = self.heap.pop()  # Pop the last element and move it to the root
            self._heapify_down(0)  # Re-heapify from the root
        return min_item

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent_index][0]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        size = len(self.heap)
        while 2 * index + 1 < size:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if left_child < size and self.heap[left_child][0] < self.heap[smallest][0]:
                smallest = left_child
            if right_child < size and self.heap[right_child][0] < self.heap[smallest][0]:
                smallest = right_child

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

# Dijkstra's Algorithm with Custom MinHeap
def dijkstra(graph, start):
    # Initialize distances: set to infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Create a MinHeap to store nodes with their distances
    heap = MinHeap()
    heap.insert((0, start))  # Insert the start node with distance 0

    while True:
        # Extract the node with the minimum distance
        min_item = heap.extract_min()
        if min_item is None:  # If heap is empty, break the loop
            break
        current_distance, current_node = min_item

        # Relaxation step: update the distance of neighboring nodes
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:  # If a shorter path is found
                distances[neighbor] = distance
                heap.insert((distance, neighbor))  # Insert or update the node in the heap

    return distances

# Example graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 1)],
    'C': [('A', 3), ('B', 1)]
}

start_node = 'A'
result = dijkstra(graph, start_node)
print(result)
