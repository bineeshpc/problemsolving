class Node:
    def __init__(self, data):
        self.data = data
        self.next = self

class CircularList:
    def __init__(self):
        self.head = Node(None)

    def prepend(self, data):
        node = Node(data)
        old_first_node = self.head.next
        if old_first_node != self.head:
            self.head.next = node
            node.next = old_first_node
        else:
            self.head.next = node
            node.next = self.head
    
    def delete(self, data):
        node = self.head.next
        while node != self.head:
            if node.next is not None:
                next_node = node.next
                if next_node.data == data:
                    # this is my node to delete
                    node.next = next_node.next
            node = node.next

    def print_list(self):
        node = self.head.next
        while node != self.head:
            print(node.data)
            node = node.next


def main():
    lst = range(10)
    cll = CircularList()
    for i in lst:
        cll.prepend(i)
    cll.print_list()



if __name__ == "__main__":
    main()