
def mergesort(a):
    return mergesorthelper(a, 0, len(a))


def mergesorthelper(a, begin, end):
    if begin < end:
        x = (begin + end) / 2
        mergesorthelper(a, begin, x)
        mergesorthelper(a, x+1, end)
        merge(a, begin, x, end)
        

"""
def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    ai = p
    b = [0] * n1
    c = [0] * n2
    b = [a[p+i] for i in range(n1)]
    c = [a[q+i] for i in range(n2)]
    print a[p:r], p, q, r, b, c
    lenb = len(b)#q - p
    lenc = len(c)#r - q - 1
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
        print ai, i
        a[ai] = b[i]
        i += 1
        ai += 1
    while j < lenc:
        a[ai] = c[j]
        j += 1
        ai += 1
    print a[p:r]
"""

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[l + i]
 
    for j in range(0 , n2):
        R[j] = arr[m + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    print i, j, k, L, R, l, m, r, arr
    # Copy the remaining elements of R[], if there
    # are any
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    
