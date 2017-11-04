class Queue:
    def __init__(self):
        self.size = 0
        self.data = []

    def enqueue(self, val):
        self.data.append(val)
        self.size = self.size + 1

    def dequeue(self):
        self.size -= 1
        return self.data.pop(0)
    
    def isempty(self):
        return self.size == 0
