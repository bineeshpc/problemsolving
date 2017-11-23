# http://www.spoj.com/problems/FCTRL2/

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1) * n

def factorial_iterative(n):
    product = n
    if n == 0 or n == 1:
        return 1
    while n > 1:
        product = product * (n - 1)
        n -= 1
    return product

def factorial_iterative_process(n):
    def factorial1(accumulator, n):
        if n == 0 or n == 1:
            return accumulator * 1
        else:
            return factorial1(accumulator * n, n - 1)
    return factorial1(1, n)

num_testcases = int(raw_input())
count = 0
while count < num_testcases:
    value = int(raw_input())
    print factorial_iterative_process(value)
    count += 1
