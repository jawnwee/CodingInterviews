from SQDS import Stack

class MyQueue():

    def __init__(self):
        self.stack = Stack()
        self.helpderStack = Stack()

    def enqueue(self, data):
        self.stack.push(data)

    def dequeue(self):
        if self.stack.isEmpty():
            return 'Queue is currently empty'
        self.createQueue()
        data = self.helperStack.pop()
        while not self.helperStack.isEmpty():
            self.stack.push(self.helpderStack.pop())

    def createQueue(self):
        while not self.stack.isEmpty():
            self.helperStack.push(self.stack.pop())
