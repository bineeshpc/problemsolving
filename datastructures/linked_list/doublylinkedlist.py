"""
h -> first -> second -> third -> None
  <- first <- second <- third
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)

    def prepend(self, data):
        node = Node(data)
        node.previous = self.head
        node.next = self.head.next
        if self.head.next:
            self.head.next.previous = node
        self.head.next = node

    def print_list(self):
        node = self.head.next
        while node != None:
            print(node.data)
            node = node.next

    def print_backwards(self):
        node = self.head.next
        while node.next != None:
            node = node.next
        while node != self.head:
            print(node.data)
            node = node.previous

def main():
    dll = DoublyLinkedList()
    lst = [2, 1, 0]
    for i in lst:
        dll.prepend(i)
    dll.print_list()
    dll.print_backwards()

if __name__ == "__main__":
    main()