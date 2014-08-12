class Stack():

    def __init__(self):
        self.stack = []
        self.minElemStack = []

    def push(self, data):
        if self.stack == []:
            self.minElemStack.append(data)
        else:
            if self.minElemStack[len(self.minElemStack) - 1] > data:
                self.minElemStack.append(data)
        self.stack.append(data)

    def pop(self):
        # if self.peek() == self.minElement():
        #     self.minElemStack.pop()
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

    def peek(self):
        if self.stack != []:
            return self.stack[len(self.stack) - 1]
        else:
            return 'Stack is empty'

    def stackSize(self):
        if self.stack != []:
            return len(self.stack)
        else:
            return 0

    def minElement(self):
        return self.minElemStack[len(self.minElemStack) - 1]

class Queue():

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        return self.queue.pop()

    def peek(self):
        return self.queue[len(self.queue) - 1]

    def isEmpty(self):
        return self.queue == []
