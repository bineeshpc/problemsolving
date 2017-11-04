
class Stack:
    def __init__(self):
        self.data = []
        self.size = 0

    def push(self, value):
        self.data.append(value)
        self.size += 1

    def pop(self):
        self.size -= 1
        data = self.data[self.size]
        del self.data[self.size]
        return data

    def __str__(self):
        return ','.join([str(i) for i in self.data])
