import heap


class PriorityQueue(heap.Heap):
    def enqueue(self, value):
        self.insert(value)

    def put(self, value):
        self.enqueue(value)

    def dequeue(self):
        self.delete()

    def get(self):
        self.dequeue()



