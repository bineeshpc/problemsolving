import searchlib
import random
import sys

def test():
    """
     When we have duplicates linear search and binary search can return different
    answers. Binary search can return the right most element, but linear search 
    will always return the left most element. There is some indeterminism 
    in binary search when there are duplicates
    """
    random.seed(42)
    a = [random.randint(1, 100) for i in range(20)]
    print(a)
    a.sort()
    print(searchlib.linear_search(a, 87))
    print(searchlib.binary_search(a, 87))
    
test()
