# First In, First Out

class Queue:
    def __init__(self, size):
        self.items = [None for _ in range(size)]
        self.size = size
        self.start = 0
        self.end = 0
        self.counter = 0

    def enqueue(self, item):
        if self.counter == self.size:
            return
        self.items[self.end] = item
        self.end = (self.end + 1) % self.size
        self.counter += 1

    def dequeue(self):
        if self.counter == 0:
            return None
        item = self.items[self.start]
        self.items[self.start] = None
        self.start = (self.start + 1) % self.size
        self.counter -= 1
        return item

    def __str__(self):
        return self.items.__str__()

    