class Edge:
    def __init__(self, source, destination, weight):
        self.weight = weight
        self.destination = destination
        self.source = source

edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]
    if source not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))


start = int(input())
target = int(input())

max_node = max(graph.keys())
