import sys
sys.path.append('../linked_list')
import linkedlist


class Stack(object):
    def __init__(self):
        """ Creates an empty stack """
        self.linked_list = linkedlist.List()
        self.linked_list.createlist([])

    def push(self, data):
        """ add an element to the stack
        Args: data
        Returns: None """
        self.linked_list.insert_in_beginning(data)

    def pop(self):
        """ Returns an element from stack
        Args: No arguments
        Returns: the data from the first element and deletes that data"""
        return self.linked_list.delete_from_beginning()

    def top(self):
        """ Returns an element from stack
        Args: No arguments
        Returns: the data from the first element without deleting that data"""
        return self.linked_list.get_first()


if __name__ == '__main__':
    s = Stack()
    for i in range(1, 11):
        s.push(i)

    print s.top().data    
    for i in range(20):
        print s.pop()
