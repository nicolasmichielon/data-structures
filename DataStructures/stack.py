# LIFO - Last In, First Out

class Stack:
    def __init__(self, size):
        self.items = [None for _ in range(size)]
        self.index = 0
        self.size = size
    
    def push(self, item):
        if self.index == len(self.items):
            return
        self.items[self.index] = item
        self.index += 1
      
    def pop(self):
        if len(self.items) == 0:
            return None
        self.index -= 1
        self.items[self.index] = None
        return self.items[self.index]

    def top(self):
        if len(self.items) == 0:
            return None
        return self.items[self.index-1]

    def viewSize(self):
        return self.index
    
    def isEmpty(self):
        return self.index == 0

    def isFull(self):
        return self.index == self.size