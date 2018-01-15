class PriorityQueue:
    def __init__(self):
        self.heapsize = 0
        self.data = []

    def percolate(self, i):

        if i >= 0 and i < self.heapsize:
            left = self.left(i)
            right = self.right(i)
            #parent = self.parent(i)
            max = i
            if left and self.data[max] < self.data[left]:
                max = left
            if right and self.data[max] < self.data[right]:
                max = right
            #print i, max, self.data[i], self.data[max], self.data,
            if max != i:
                tmp = self.data[max]
                self.data[max] = self.data[i]
                self.data[i] = tmp
                self.percolate(max)
            #print self.data



            
    def buildheap(self, a):
        self.data = a
        length = len(a)
        self.heapsize = length
        for i in range((length-2)/2, -1, -1):
            self.percolate(i)

        
    def parent(self, i):
        val = (i - 1) / 2
        if val >= 0 and val < self.heapsize:
            return val
    
    def left(self, i):
        val = 2 * i + 1
        if val >= 0 and val < self.heapsize:
            return val        
    
    def right(self, i):
        val = 2 * i + 2
        if val >= 0 and val < self.heapsize:
            return val
    
    def heapsort(self):
        for i in range(self.heapsize, 0, -1):
            elem = self.data[0]
            self.data[0] = self.data[self.heapsize - 1]
            self.data[self.heapsize - 1] = elem
            self.heapsize -= 1
            self.percolate(0)
            #print "size=", self.heapsize, "data=",self.data[0:self.heapsize], self.data
        