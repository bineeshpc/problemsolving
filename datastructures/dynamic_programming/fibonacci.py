def fibonacci_bottomup(n):
    """ dynamic programming memoization in a bottom up way 
    In bottom up dynamic programming we do a
    topological sort of the dependency graph
    and then we do the computation in that order
    In this particular case since we need to remember only
    2 previous fibonacci numbers we can actually 
    use just two variables instead of an array with
    all fiboanacci values from 0 to n
    """
    if n < 0:
        raise Exception('undefined for negative numbers')
    fib = [0, 1]
    for i in range(2, n+1):
        fibval = fib[i-1] + fib[i-2]
        fib.append(fibval)
    return fib[n]


def fibonacci_topdown(n):
    """ dynamic programming memoization in a top down way """
    if n < 0:
        raise Exception('undefined for negative numbers')
    fibstore = {0: 0, 1: 1}
    if n in fibstore:
        return fibstore[n]
    else:
        fibstore[n] = fibonacci_topdown(n-1) + fibonacci_topdown(n-2)
    return fibstore[n]


def fibonacci_iterative(n):
    """
    In this particular case since we need to remember only
    2 previous fibonacci numbers we can actually 
    use just two variables instead of an array with
    all fiboanacci values from 0 to n
    
    """
    if n < 0:
        raise Exception('undefined for negative numbers')
    if n == 0 or n == 1:
        return n
    fib_iminus2 = 0
    fib_iminus1 = 1
    for i in range(2, n+1):
        fib = fib_iminus1 + fib_iminus2
        fib_iminus2 = fib_iminus1
        fib_iminus1 = fib
    return fib


for i in range(10):
    print fibonacci_bottomup(i) == fibonacci_topdown(i) == fibonacci_iterative(i)

#for i in range(-1, 0):
#    print fibonacci_bottomup(i) == fibonacci_topdown(i) == fibonacci_iterative(i)
    
