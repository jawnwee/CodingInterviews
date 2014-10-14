class Queue():

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        return self.queue.pop()

    def peek(self):
        return self.queue[len(self.queue) - 1]

    def print_all_items(self):
        for q in self.queue:
            print(q)

    def isEmpty(self):
        return self.queue == []
