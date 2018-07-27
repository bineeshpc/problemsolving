import random
import quicksort

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


def partition(arr, p, r):
    """ After partition is keep the r th element in the right position
    Let us call the r th element as pivot element
    We modify the array such that every element before the pivot is 
    less than the pivot element and every element coming after the pivot element 
    is greater than the pivot element
    Finally we return the right position of the pivot element
    """
    random_r = random.randint(p, r) # improve the performance of quicksort by
                                    # introducing randomness
    arr[random_r], arr[r] = arr[r], arr[random_r] # swap elements
    pivot = arr[r]  # pivot is the last element in the array
    i = p - 1  # i+1 is the position to swap with j after finding
               # an element which is less than pivot
    j = p  # j attempts to find an element that is less than pivot
    #  loop invariant every element upto ith index from p is less than pivot
    while j < r:  # j values from p to r
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # swap arr[i] and arr[j]
        j += 1
    # every element from p to i is less than pivot
    # now we know that i + 1 is the right position for pivot
    # swap position i + 1 with r
    arr[i+1], arr[r] = arr[r], arr[i+1]  # swap arr[i+1] and arr[r]
    
    return i + 1


def quicksorthelper(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksorthelper(a, p, q-1)
        quicksorthelper(a, q+1, r)


def quicksort(arr):
    """ Uses quicksort algorithm to sort an array """
    quicksorthelper(arr, 0, len(arr) - 1)

