#!/bin/python3

"""
https://www.hackerrank.com/contests/goldman-sachs-womens-codesprint/challenges/stock-exchange-matching-algorithm
4
12 15 1 50
7 32 43 77
4
1
12
100
1000

0 1  2  3
1 12 15 50

0 3
1



"""


import math
import os
import random
import re
import sys

#
# Complete the 'computePrices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER_ARRAY p
#  3. INTEGER_ARRAY q
#


def binary_search(s, n):
    begin = 0
    end = len(s) - 1
    mid = (begin + end) // 2
    while begin <= end:
        mid = (begin + end) // 2
        if s[mid][0] > n:
            end = mid - 1
        elif s[mid][0] < n:
            begin = mid + 1
        else:
            return s[mid][1]
    try:
        if s[end][0] < n:
            return s[end][1]
        else:
            if s[begin][0] > n:
                return s[begin-1][1]
            else:
                i = end
                while s[i][0] > n:
                    out = s[i][1]
                    i -= 1
                return out
    except:
        pass



        

def computePrices(s, p, q):
    # Write your code here
    sp = list(zip(s, p))
    sp.sort()
    output = []
    for qi in q:
        output.append(binary_search(sp, qi))
    return output
         
        
        

if __name__ == '__main__':
    fptr = open('out.txt', 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    p = list(map(int, input().rstrip().split()))

    k = int(input().strip())

    q = []

    for _ in range(k):
        q_item = int(input().strip())
        q.append(q_item)

    res = computePrices(s, p, q)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
