import sys

empty_value = -5
class Stack:
    def __init__(self, max_size=100):
        """ Initializes stack content to empty list """
        self.max_size = max_size
        self.data = [empty_value for i in range(self.max_size)]
        self.size = 0

    def push(self, value):
        """ Add an element to stack """
        self.data[self.size] = value
        self.size += 1

    def pop(self):
        """ Remove and return the element from the top of the stack """
        if self.size > 1:
            self.size -= 1
            data = self.data[self.size]
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
        """ Returns a string of stack elements.
            Limit the elements to be displayed to 100
        """
        max_size = 100
        if self.size > max_size:
            sys.stdout.write("reducing the size to {}".format(max_size))
        return ','.join([str(self.data[i]) for i in range(max_size)])
