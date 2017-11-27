# http://www.spoj.com/problems/AE00/
import math


def get_factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append((i, n / i))
    return factors

def get_num_rectangles(n):
    count = 0
    if n == 0:
        return 0
    else:
        count += len(get_factors(n)) + get_num_rectangles(n-1)
    return count

def get_num_rectangles_iterative(n):
    count = 0
    for i in range(n+1):
        count += len(get_factors(i))
    return count

def process():
    num = int(raw_input())
    print get_num_rectangles_iterative(num)

process()
