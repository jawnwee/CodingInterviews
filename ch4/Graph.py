class Graph(object):
    def __init__(self):
        self.graphDictionary = {}

    def addNode(self, node):
        if self.graphDictionary[node] != []:
            return 'Node already exists'
        self.graphDictionary[node] = []

    def addEdge(self, frm, to):
        if self.graphDictionary[frm] and self.graphDictionary[to]:
                self.graphDictionary[frm].append(to)
        else:
            return 'Cannot create edge to non-existant nodes'
