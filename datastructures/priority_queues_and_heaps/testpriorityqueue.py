import priorityqueue as pq
import random

class Test:
    def setUp(self):
        self.data = [random.randint(1, 10000) for i in range(100)]
        print self.data
        
    def testbuildheap(self):
        print "testing build heap"
        queue = pq.PriorityQueue()
        queue.buildheap(self.data)
        print queue.data
        print "done testing build heap"
        
    def testheapsort(self):
        print "testing heapsort"
        queue = pq.PriorityQueue()
        print "building heap for heapsort"
        queue.buildheap(self.data)
        print queue.data
        print "Going to call heapsort"
        queue.heapsort()
        print queue.data
        assert queue.data == sorted(self.data)