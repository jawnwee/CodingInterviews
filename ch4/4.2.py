from Graph import Graph
from Stack import Stack

stack = Stack()

def routeExists(graph, a, b):
    if a == b:
        return True
    if graph.graphDictionary[a] = []:
        return False
    a_edges_nodes = graph.graphDictionary[a]
    for node in a_edges_nodes:
        if node == b:
            return True
        stack.push(node)
    while not stack.isEmpty():
        node = stack.pop()
        return routeExists(graph, node, b)

