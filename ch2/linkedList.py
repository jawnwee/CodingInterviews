class Node:

    def __init__(self, data=None, nextNode = None):
        self.data = data
        self.nextNode = nextNode

    def addNodeToTail(self, d):
        end = d
        n = self
        while n.nextNode != None:
            n = n.nextNode
        n.nextNode = end

    def addNodeToFront(self, d):
        front = Node(d)
        front.nextNode = self
        self.head = front

    def addToTail(self, d):
        end = Node(d)
        n = self
        while n.nextNode != None:
            n = n.nextNode
        n.nextNode = end

    def printValues(self):
        while self != None:
            print(self.data)
            self = self.nextNode
