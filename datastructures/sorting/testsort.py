import mergesort
import quicksort
import random

def testqs():
    a = [random.randint(1, 100) for i in range(10)]
    b = a[:]
    print quicksort.quicksort_haskell_style(a)
    assert quicksort.quicksort_haskell_style(a) == sorted(b)

def testpartition():
    a = [random.randint(1, 100) for i in range(10)]
    r = len(a) - 1
    q = quicksort.partition(a, 0, r)
    print a, q
    x = a[q]
    assert all([a[i] <= x for i in range(0, q)])
    assert all([a[i] >= x for i in range(q+1, r)])

def tquicksort(size):
    a = [random.randint(1, 100) for i in range(size)]
    b = a[:]
    quicksort.quicksort(a)
    print a
    c = sorted(b)
    print c
    assert a == c

def testquicksort():
    for i in range(0, 100):
        tquicksort(i)
"""
class TestSort:
    def setUp(self):
        self.array =  [random.randint(1, 100) for i in range(10)]
        
    def testmergesort(self):
        newarray = self.array[::]
        newarray1 = self.array[::]
        print self.array
        mergesort.mergesort(newarray)
        print newarray
        print sorted(newarray1)




# quicksort([5, 4, 1, 2, 7, 6, 3])


import random
a =  [random.randint(1, 100) for i in range(10)]
a = [34, 74, 94, 21, 93, 62, 100, 67, 10, 61]
print a, len(a)
mergesort(a)
print a


"""
