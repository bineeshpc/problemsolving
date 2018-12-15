import random
import time


def quicksort_haskell_style(arr):
    """
    Quicksort in python which is similar to the haskell version
    https://wiki.haskell.org/Introduction#Quicksort_in_Haskell
    """
    if arr == []:
        return []
    else:
        lesser = [i for i in arr[1:] if i < arr[0]]
        greater = [i for i in arr[1:] if i >= arr[0]]
        return quicksort_haskell_style(lesser) \
            + [arr[0]] \
            + quicksort_haskell_style(greater)


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def partition_corman(arr, p, r):
    """ After partition is keep the r th element in the right position
    Let us call the r th element as pivot element
    We modify the array such that every element before the pivot is
    less than the pivot element and every element coming after the
    pivot element is greater than the pivot element
    Finally we return the right position of the pivot element
    """
    random_r = random.randint(p, r)  # improve the performance of quicksort by
    # introducing randomness
    swap(arr, random_r, r)
    pivot = arr[r]  # pivot is the last element in the array
    i = p - 1  # i+1 is the position to swap with j after finding
    # an element which is less than pivot
    j = p  # j attempts to find an element that is less than pivot
    #  loop invariant every element upto ith index from p is less than pivot
    while j < r:  # j values from p to r
        if arr[j] < pivot:
            i = i + 1
            swap(arr, i, j)
        j += 1
    # every element from p to i is less than pivot
    # now we know that i + 1 is the right position for pivot
    swap(arr, i + 1, r)
    return i + 1


def partition_internet(arr, lo, hi):
    too_big_index = lo
    too_small_index = hi
    # too_big_index is an index with element less than pivot
    # too_small_index is an index with element greater than pivot
    # introduce randomness for improving quicksort
    random_lo = random.randint(lo, hi)
    swap(arr, lo, random_lo)
    pivot = arr[lo]
    while too_big_index < too_small_index:
        # loop invariant
        # for every index < too_big_index arr[index] <= pivot
        # are less than pivot except the pivot index
        while arr[too_big_index] <= pivot and too_big_index < hi:
            too_big_index += 1
        # now we know the element which is too big to be on LHS

        # loop invariant
        # for every index > too_small_index arr[index] > pivot
        while arr[too_small_index] > pivot and too_small_index > lo:
            too_small_index -= 1
        # now we know an element which is too small to be on the RHS
        if too_big_index < too_small_index:
            swap(arr, too_big_index, too_small_index)
    swap(arr, lo, too_small_index)
    return too_small_index


partition = partition_corman


def quicksorthelper(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksorthelper(a, p, q - 1)
        quicksorthelper(a, q + 1, r)


def quicksort(arr):
    """ Uses quicksort algorithm to sort an array """
    quicksorthelper(arr, 0, len(arr) - 1)


def sort(arr):
    """ Just a facade to simplify
    """
    quicksort(arr)


def time_it(function):
    def timed_function(*args, **kwargs):
        ts = time.time()
        result = function(*args, **kwargs)
        te = time.time()
        print("executed in {} seconds".format(te - ts))
        return result
    return timed_function


@time_it
def sort1(arr):
    sort(arr)


@time_it
def sort2(arr):
    arr.sort()


def main():
    value = 10**6
    arr = [random.randint(0, value) for i in range(value)]
    arr_copy1 = [i for i in arr]
    arr_copy2 = [i for i in arr]
    arr_copy3 = [i for i in arr]
    globals()['partition'] = partition_corman
    sort1(arr_copy1)
    globals()['partition'] = partition_internet
    sort1(arr_copy2)
    sort2(arr_copy3)
    assert arr_copy1 == arr_copy2 == arr_copy3
    if value <= 20:
        print(arr)
        print(arr_copy1)
        print(arr_copy2)


if __name__ == '__main__':
    main()
