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

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class QueueList:
    def __init__(self):
        self.head = Node(None)
        self.lastnode = self.head

    def put(self, data):
        newnode = Node(data)
        self.lastnode.next = newnode
        self.lastnode = self.lastnode.next

    def get(self):
        node = self.head.next
        if node is not None:
            data = node.data
            self.head.next = node.next
            if node.next is None:
                self.lastnode = self.head
            return data
        else:
            print('queue empty')

    def put(self, data):
        newnode = Node(data)
        self.lastnode.next = newnode
        self.lastnode = newnode

    def isempty(self):
        if self.lastnode == self.head:
            return True
        else:
            return False

def test_queuelist():
    q = QueueList()
    q.put(1)
    q.put(2)

    for i in range(2):
        print(q.get())

test_queuelist()
