class Heap(object):
    """ Heap datastructure represented as an array """
    def __init__(self, maxsize):
        self.heapsize = 0
        self.maxsize = maxsize
        self.data = [0] * self.maxsize

    def insert(self, element):
        """ Inserts an element in the heap
        Ensure that heap property is still maintained"""
        if self.maxsize > self.heapsize:
            self.heapsize += 1
        else:
            raise Exception("heap full")
        self.data[self.heapsize - 1] = element
        self.percolate_up(self.heapsize - 1)
        

    def delete(self):
        """ Deletes the max element from the heap """
        temp = self.data[0]
        self.data[0] = self.data[self.heapsize - 1]
        self.data[self.heapsize - 1] = temp
        self.heapsize -= 1
        self.percolate_down(0)
        return temp

    def parent(self, index):
        """ math.floor((n-1)/2)"""
        return (index-1)/2

    def children(self, index):
        """ children of the node with index n"""
        return ((index * 2) + 1, (index * 2) + 2)

    def percolate_down(self, index):
        """ Find the right node for the present data and put the
        data in that position """
        if index < self.heapsize - 1:
            left, right = self.children(index)
            if right > self.heapsize-1:
                return
            max_index = left
            if self.data[max_index] < self.data[right]:
                max_index = right
            if self.data[index] < self.data[max_index]:
                temp = self.data[index]
                self.data[index] = self.data[max_index]
                self.data[max_index] = temp
                self.percolate_down(max_index)


    def percolate_up(self, index):
        """ Find the right node for the present data and 
        put data in that position """
        if index > 0:
            parent = self.parent(index)
            if self.data[index] > self.data[parent]:
                temp = self.data[index]
                self.data[index] = self.data[parent]
                self.data[parent] = temp
                self.percolate_up(parent)

    def heapsort(self):
        initial_size = self.heapsize
        while self.heapsize > 0:
            self.delete()
        sorted_data = []
        for i in range(initial_size):
            sorted_data.append(self.data[i])
        return sorted_data

    def print_heap(self):
        for i in range(self.heapsize-1):
            print self.data[i], ',',
        print self.data[self.heapsize-1]


if __name__ == '__main__':
    heap = Heap(100)
    for i in range(25, 50):
        heap.insert(i)

    heap.print_heap()

    print heap.heapsort()
    
