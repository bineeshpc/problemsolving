class Stack:
    def __init__(self):
        """ Initializes stack content to empty list """
        self.data = []
        self.size = 0

    def push(self, value):
        """ Add an element to stack """
        self.data.append(value)
        self.size += 1

    def pop(self):
        """ Remove and return the element from the top of the stack """
        if self.size > 1:
            self.size -= 1
            data = self.data[self.size]
            del self.data[self.size]
            return data
        else:
            return None

    def peek(self):
        """ Returns the top element of the stack but does not delete it """
        if self.size > 0:
            return self.data[self.size - 1]
        else:
            return None

    def __str__(self):
        return ','.join([str(i) for i in self.data])
