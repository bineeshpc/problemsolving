import quicksort
import random

def shuffle_sort(arr):
    """ 
    Generate a random number associated with every number and sort it
    This takes n log n time
    """
    arr1 = [(random.random(), x) for x in arr]
    quicksort.quicksort(arr1)
    return [y for x, y in arr1]


def knuth_shuffle(arr):
    """
    Shuffle the array in O(n)
    We keep a loop invariant where elements from 0 - i is shuffled
    Once we reach the end of the loop every element is shuffled
    """

    i = 0
    length = len(arr) - 1
    while i <= length:
        position = random.randint(i, length)
        arr[position], arr[i] = arr[i], arr[position] # swaps 2 positions
        i += 1
    return arr

