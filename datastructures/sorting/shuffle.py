import quicksort
import random


def sort_shuffle(arr):
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
        arr[position], arr[i] = arr[i], arr[position]  # swaps 2 positions
        i += 1
    return arr


def my_shuffle(arr):
    """
    Shuffle the array in O(n)
    Generate two random numbers from left side and right side
    choose one from these two to swap with the the ith position
    i moving from 0 to length - 1
    This one is complicated and I don't like this
    """
    i = 0
    length = len(arr) - 1
    two_nums = [0, 0]
    while i <= length:
        if i > 0:
            two_nums[0] = random.randint(0, i - 1)
        else:
            two_nums[0] = 0
        if i < length:
            two_nums[1] = random.randint(i + 1, length)
        else:
            two_nums[1] = length
        num = random.choice(two_nums)
        arr[i], arr[num] = arr[num], arr[i]
        i += 1
    return arr
