def quicksort_haskell_style(arr):
    """
    Quicksort in python which is similar to the haskell version
    https://wiki.haskell.org/Introduction#Quicksort_in_Haskell
    """
    if arr == []:
        return []
    else:
        lesser = [i for i in arr if i < arr[0]]
        greater = [i for i in arr if i > arr[0]]
        return quicksort_haskell_style(lesser) \
            + [arr[0]] \
            + quicksort_haskell_style(greater)


def partition(a, p, r):
    x = a[r-1]  # x is the last element in the array
    i = p - 1
    j = p
    while j < r - 1:  # j values from p to r - 1
        print i, j, a, x
        if a[j] < x:
            i = i + 1
            a[i], a[j] = a[j], a[i]  # swap a[i] and a[j]
        j += 1
        print i, j, a, x
    a[i+1], a[r-1] = a[r-1], a[i+1]  # swap a[i+1] and a[r-1]
    return i + 1


def quicksorthelper(a, p, r):
    if p < r:
        q = partition(a, p, r)
        print q, a
        quicksorthelper(a, p, q)
        quicksorthelper(a, q+1, r)


def quicksort(arr):
    """ Uses quicksort algorithm to sort an array """
    quicksorthelper(arr, 0, len(arr))


def mergesort(a):
    return mergesorthelper(a, 0, len(a))


def mergesorthelper(a, begin, end):
    if begin < end:
        x = (begin + end) / 2
        mergesorthelper(a, begin, x)
        mergesorthelper(a, x+1, end)
        merge(a, begin, x, end)


def merge(a, p, q, r):
    ai = p
    b = a[p:q]
    c = a[q+1:r]
    lenb = q - p + 1 - 1
    lenc = r - q - 1
    i = 0
    j = 0
    while i < lenb and j < lenc:
        if b[i] < c[j]:
            a[ai] = b[i]
            i += 1
        else:
            a[ai] = c[j]
            j += 1
        ai += 1
    while i < lenb:
        a[ai] = b[i]
        i += 1
        ai += 1
    while j < lenc:
        a[ai] = c[j]
        j += 1
        ai += 1


quicksort([5, 4, 1, 2, 7, 6, 3])
