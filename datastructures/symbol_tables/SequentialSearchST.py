import sys
import testlib

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SequentialSearchST:
    def __init__(self):
        self.head = None
        self.count = 0

    def put(self, key, value):       
        # check for presence of key
        # and replace it with new value
        node = self.head
        while node != None:
            if node.key == key:
                node.value = value
                return
            node = node.next
        # key was not found
        # in the symbol table
        # add the key, value pair
        node = Node(key, value)
        node.next = self.head
        self.head = node
        self.count += 1

    def get(self, key):
        node = self.head
        while node != None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def contains(self, key):
        node = self.head
        while node != None:
            if node.key == key:
                return True
            node = node.next
        return False

    def __iter__(self):
        self.iterhelper = self.head
        return self

    def __next__(self):
        node = self.iterhelper
        if node == None:
            raise StopIteration
        else:
            self.iterhelper = node.next
            return node

    def size(self):
        return self.count

    def isempty(self):
        return self.count == 0

    def delete(self, key):
        if self.head:
            if self.head.key == key:
                self.head = None
                self.count -= 1
            else:
                previous_node = self.head
                node_to_delete = previous_node.next
                while node_to_delete != None:
                    if node_to_delete.key == key:
                        previous_node.next = node_to_delete.next
                        self.count -= 1
                    previous_node = node_to_delete
                    node_to_delete = node_to_delete.next
            

def main():
    st = SequentialSearchST()
    testlib.test_SequentialSearchST(st)

if __name__ == '__main__':
    main()