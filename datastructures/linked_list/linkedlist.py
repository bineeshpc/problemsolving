#! /usr/bin/env python
import six

class Node(object):
    """ Represents a single node in the linked list which can
    be used in the list data structure
    """
    def __init__(self, data):
        """ Create a single node using this function.
        All node's will have its next element initialized to None
        """
        self.data = data
        self.next = None


class List(six.Iterator):
    def __init__(self):
        """ Initializes a header node with data as None
        we don't store data in the header"""
        self.head = Node(None)

    def insert(self, data):
        """ Given an element insert it in to the end of the list """
        node = Node(data)
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = node
        return node


    def insert_in_beginning(self, data):
        """ inserts a node in the beginning of data
        Args: data
        returns: None """
        node = Node(data)
        temp = self.head.next
        self.head.next = node
        node.next = temp


    def delete_from_beginning(self):
        """ Deletes a node in the beginning of list
        Args: data
        returns: the data from deleted node """
        temp = self.head.next
        if temp:
            self.head.next = temp.next
            return temp.data
        

    def get_first(self):
        """ Gets the first node from the list 
        Args: No arguments
        Returns: First node in the linked list """
        return self.head.next
        
    def createlist_inefficient(self, lst):
        """ For every element we start from the head
        We insert the element in the end"""
        for i in lst:
            self.insert(i)

    def createlist(self, lst):
        """ This is efficient implementation of create list
        Args: lst is a python list which is used to construct a linked list
        """
        node = None
        firstnode = None
        for element in lst:
            if not node:
                node = Node(element)
                firstnode = node
            else:
                node.next = Node(element)
                node = node.next
        self.head.next = firstnode

    def search(self, data):
        """ Searches the linkes list and returns True if found
        returns False if not found
        Args: data
        Returns: True if found else returns False """
        runner = self.head
        while runner.next is not None:
            runner = runner.next
            if runner.data == data:
                return True
        return False

    def delete(self, data):
        """ Deletes the node with data == data
        Args: data which is the element to delete if present in list
        Returns: False if not found """
        runner = self.head
        while runner.next is not None:
            if runner.next.data == data:
                runner.next = runner.next.next
                return True  # found data and deleted
            else:
                runner = runner.next
        return False  # did not find the element

    def createcycle(self, initialrun, cyclesize):
        """ Creates a linked list with a cycle where there
        is an initial run of lenght initial run and
        a cycle size of cycle size
        Args: 
        initialrun int with a initial run count initialrun
        cyclesize int with cycle size cyclesize
        Returns: None """
        # create initial run of 1 to initialrun without cycle
        for element in range(1, initialrun + 1):
            node = self.insert(element)
        # create cycle
        node1 = node
        for count in range(cyclesize):
            node1.next = Node(initialrun + count)
            node1 = node1.next
        node1.next = node

    def detectcycle(self):
        """ detects a cycle if present in a linked list
        """
        hare = self.head
        tortoise = self.head
        while hare.next is not None:
            if hare.next.next is not None:
                hare = hare.next.next
                tortoise = tortoise.next
            else:
                break
            if hare == tortoise:
                six.print_("Cycle detected")
                return True
        six.print_("no cycle detected")
        return False

    def __str__(self):
        """ return the str form of a non cyclical linked list """
        runner = self.head
        lst = ["H"]
        runner = runner.next
        while runner is not None:
            lst.append("->{}".format(runner.data))
            runner = runner.next
        return ''.join(lst)

    def tolist(self):
        """ Convert a linked list to a normal list """
        lst = []
        runner = self.head
        while runner.next is not None:
            lst.append(runner.next.data)
            runner = runner.next
        return lst

    def isempty(self):
        """ Checks whether the list is empty
        """
        return self.head.next == None

    def __iter__(self):
        self.iterhelper = self.head
        return self


    def __next__(self):
        self.iterhelper = self.iterhelper.next
        if self.iterhelper is None:
            raise StopIteration
        return self.iterhelper.data
