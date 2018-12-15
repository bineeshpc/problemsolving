
def mergesort(a):
    temp = [0 for i in range(len(a))]
    mergesorthelper(a, 0, len(a) - 1, temp)
    return a


def mergesorthelper(a, lo, hi, temp):
    if lo < hi:
        mid = (lo + hi) // 2
        mergesorthelper(a, lo, mid, temp)
        mergesorthelper(a, mid + 1, hi, temp)
        merge(a, lo, mid, hi, temp)


def merge(a, lo, mid, hi, temp):
    """ a[lo..mid] and a[mid+1..hi] are sorted subarrays of a
    Merge these two sorted subarrays into corresponding positions of a
    """
    # copy a[lo..mid] to temp[lo..mid]
    for i in range(lo, mid+1):
        temp[i] = a[i]
    # copy a[mid+1] to temp[mid+1..end]
    for i in range(mid+1, hi+1):
        temp[i] = a[i]

    i = lo
    j = mid + 1
    k = lo

    while i <= mid and j <= hi:
        if temp[i] <= temp[j]:
            a[k] = temp[i]
            i += 1
        else:
            a[k] = temp[j]
            j += 1
        k += 1

    while i <= mid:
        a[k] = temp[i]
        k += 1
        i += 1

    while j <= hi:
        a[k] = temp[j]
        k += 1
        j += 1


def mergesorthelper1(a, begin, end):
    if begin < end:
        mid = (begin + end) // 2
        mergesorthelper(a, begin, mid)
        mergesorthelper(a, mid + 1, end)
        merge(a, begin, mid, end)


# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge1(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
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
    # print(i, j, k, L, R, l, m, r, arr)
    # Copy the remaining elements of R[], if there
    # are any

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
