import priorityqueue as pq
import random

class TestPriorityQueue:

    def testheapsort(self):
        self.data = [random.randint(1, 10000) for i in range(200)]
        length = len(self.data)
        queue = pq.PriorityQueue(length)
        for i in self.data:
            queue.insert(i)
        queue.heapsort()
        print(queue.data)
        print(sorted(self.data))
        assert queue.data == sorted(self.data)

    def test_with_tuple_max(self):
        self.data = [(i, i) for i in range(10)]
        random.shuffle(self.data)
        length = len(self.data)
        queue = pq.PriorityQueue(length)
        for i in self.data:
            queue.insert(i)
        queue.heapsort()
        print(queue.data)
        print(sorted(self.data))
        assert queue.data == sorted(self.data)


    def test_with_tuple_min(self):
        self.data = [(-i, i) for i in range(10)]
        random.shuffle(self.data)
        length = len(self.data)
        queue = pq.PriorityQueue(length)
        for i in self.data:
            queue.insert(i)
        queue.heapsort()
        print(queue.data)
        print(sorted(self.data))
        assert queue.data == sorted(self.data)
