import sys
import time

length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def rod_cutting_simple_recursion(price, n):
    """
    A rod of length n should be cut and sold
    Find the cutting size to maximize profit
    
    each rod of length n can be cut at 
    1 to n places(either cut it at 1 to n-1 places or without cutting at n)
    
    n = 0 -> price = 0
    else if n > 0
    max(price[i], rate[i] + rate[n-i]) 
    1<=i<=n

    """
    if n <= 0:
        return 0
    else:
        present_maximum = -sys.maxint  # initializing to -infinity
        for i in range(1, n+1):  # 1<=i<=n
            # price[i-1] because array is 0 indexed
            # price of ith item is present at i-1 th index
            present_maximum = max(present_maximum, price[i-1] + rod_cutting_simple_recursion(price, n-i))
            # price for the rod without cutting is also included in this formula because
            # when i=n, n-i = 0 and we get price[i-1] + 0 = price[i-1]
        return present_maximum


def rod_cutting_memoization(price, n):
    cache = [0 for i in range(n)]
    def rod_cutting_helper(price, n, cache):
        if n == 0:
            return 0
        if cache[n-1] != 0:
            return cache[n-1]
        else:
            present_maximum = -sys.maxint
            for i in range(1, n+1):
                present_maximum = max(present_maximum, price[i-1] + rod_cutting_helper(price, n-i, cache))
            cache[n-1] = present_maximum
            return cache[n-1]

    return rod_cutting_helper(price, n, cache)


def rod_cutting_bottom_up(price, n):
    """
    compute the smaller values first and iteratively compute 
    the larger values
    There is a dependency from smaller values to larger values
    if you think about it as a dag, topologically sort the dag 
    and compute the things in that topological order

    Example run:
    price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 2
    rates = {-1: 0, 0: 1, 1: 5}
    i from 1 to 2
        present_max = -infinity
        j from 1 to i
            i = 1, j = 1
            present_max = max(-infinity, price[1-1] ie price[0] ie 1 + rates[1-1-1] ie rates[-1] = 0)
                        = max(-infinity, 1 + 0)
                        = 1
        rates[0] = 1
        
        next iteration 
        i = 2
        j from 1 to 2
             i = 2 j = 1
             present_max = max(-infinity, 2) = 2
             i = 2 j = 2
             present_max = max(2, price[j-1] + rates[i-j-1])
                          = max(2, 5 + 0)
                          = 5
        rates[1] = 5     
    """
    rates = {i:0 for i in range(-1, n)} # indexing starts at 0, rates[-1 upto n] all assigned to 0

    for i in range(1, n+1): 
        present_max = -sys.maxint
        for j in range(1, i+1):
            present_max = max(present_max, price[j-1] + rates[i-j-1])
        rates[i-1] = present_max
    return rates[n-1]



def rod_cutting_bottom_up_with_solution(price, n):
    """
    compute the smaller values first and iteratively compute 
    the larger values
    There is a dependency from smaller values to larger values
    if you think about it as a dag, topologically sort the dag 
    and compute the things in that topological order
     
    """
    rates = {i:0 for i in range(-1, n)} # indexing starts at 0, rates[-1 upto n] all assigned to 0
    sizes = [0 for i in range(-1, n)]
    for i in range(1, n+1): 
        present_max = -sys.maxint
        for j in range(1, i+1):
            if (price[j-1] + rates[i-j-1]) > present_max:
                present_max = price[j-1] + rates[i-j-1]
                sizes[i] = j
        rates[i-1] = present_max

    length_remaining = n
    output = []
    while(length_remaining > 0):
        output.append(sizes[length_remaining])
        length_remaining = length_remaining - sizes[length_remaining]
        
    return rates[n-1], output



for i in range(0, 10):
    print i, rod_cutting_simple_recursion(price, i), rod_cutting_memoization(price, i), rod_cutting_bottom_up(price, i), rod_cutting_bottom_up_with_solution(price, i)
