import sort
import random

def testqs():
    a = [random.randint(1, 100) for i in range(10)]
    b = a[:]
    print sort.qs(a)
    assert sort.qs(a) == sorted(b)

def testpartition():
    a = [random.randint(1, 100) for i in range(10)]
    r = len(a)
    q = sort.partition(a, 0, r)
    print a, q
    x = a[q]
    assert all([a[i] <= x for i in range(0, q)])
    assert all([a[i] >= x for i in range(q+1, r)])

def quicksort(size):
    a = [random.randint(1, 100) for i in range(size)]
    b = a[:]
    sort.quicksort(a)
    print a
    c = sorted(b)
    print c
    assert a == c

def testquicksort():
    for i in range(0, 100):
        quicksort(i)

class TestSort:
    def setUp(self):
        self.array =  [random.randint(1, 100) for i in range(10)]
        
    def testmergesort(self):
        newarray = self.array[::]
        newarray1 = self.array[::]
        print self.array
        sort.mergesort(newarray)
        print newarray
        print sorted(newarray1)