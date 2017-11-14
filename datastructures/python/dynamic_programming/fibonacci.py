def fibonacci_bottomup(n):
    """ dynamic programming memoization in a bottom up way """
    fib = [0, 1]
    for i in range(2, n+1):
        fibval = fib[i-1] + fib[i-2]
        fib.append(fibval)
    return fib[n]


def fibonacci_topdown(n):
    """ dynamic programming memoization in a top down way """
    fibstore = {0: 0, 1: 1}
    if n in fibstore:
        return fibstore[n]
    else:
        fibstore[n] = fibonacci_topdown(n-1) + fibonacci_topdown(n-2)
    return fibstore[n]


def fibonacci_iterative(n):
    fib0 = 0
    fib1 = 1
    if n == 0:
        return fib0
    if n == 1:
        return fib1
    for i in range(2, n+1):
        fib = fib0 + fib1
        fib0 = fib1
        fib1 = fib
    return fib


for i in range(10):
    print fibonacci_bottomup(i) == fibonacci_topdown(i) == fibonacci_iterative(i)
