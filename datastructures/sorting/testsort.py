import mergesort
import quicksort
import random


def testqs():
    a = [random.randint(1, 100) for i in range(10)]
    b = a[:]
    print(quicksort.quicksort_haskell_style(a))
    assert quicksort.quicksort_haskell_style(a) == sorted(b)


def testpartition():
    a = [random.randint(1, 100) for i in range(10)]
    r = len(a) - 1
    q = quicksort.partition(a, 0, r)
    print(a, q)
    x = a[q]
    assert all([a[i] <= x for i in range(0, q)])
    assert all([a[i] >= x for i in range(q+1, r)])


def tquicksort(size):
    a = [random.randint(1, 100) for i in range(size)]
    b = a[:]
    quicksort.quicksort(a)
    print(a)
    c = sorted(b)
    print(c)
    assert a == c


def testquicksort():
    for i in range(0, 100):
        tquicksort(i)


def test_mergesort():
    a = [random.randint(1, 1000) for i in range(1000)]
    b = a[:]
    m = mergesort.mergesort(b)
    s = sorted(a)
    print(s)
    print(m)
    assert m == s
    
