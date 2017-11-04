class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List():
    def __init__(self):
        self.head = Node(None)

    def insert(self, data):
        node = Node(data)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = node
        return node

    def createlist(self, lst):
        for i in lst:
            self.insert(i)

    def search(self, data):
        runner = self.head
        while runner.next != None:
            runner = runner.next
            if runner.data == data:
                return data

    def delete(self, data):
        runner = self.head
        while runner.next != None:
            if runner.next.data == data:
                 runner.next = runner.next.next
                 break
            else:
                 runner = runner.next

    def createcycle(self, initialrun, cyclesize):
        #create initial run without cycle
        for i in range(1, initialrun + 1):
            node = self.insert(i)
        #create cycle
        node1 = node
        for i in range(cyclesize):
            node1.next = Node(i)
        node1.next = node
            
    def detectcycle(self):
        hare = self.head
        tortoise = self.head
        while hare.next != None:
            if hare.next.next != None:
                hare = hare.next.next
                tortoise = tortoise.next
            else: break
            if hare == tortoise:
                print "Cycle detected"
                return True
        print "no cycle detected"
        return False

    def __str__(self):
        runner = self.head
        lst = ["H"]
        runner = runner.next
        while runner != None:
            lst.append("->{}".format(runner.data))
            runner = runner.next
        return ''.join(lst)

    def tolist(self):
        lst = []
        runner = self.head
        while runner.next != None:
            lst.append(runner.next.data)
            runner = runner.next
        return lst
