"""
https://www.hackerrank.com/contests/goldman-sachs-womens-codesprint/challenges/elevator-travel

3
1 3 2

ans 

3
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def get_distance(p, i):
    d = 0
    if i >= len(p):
        return d

    if i - 1 >= 0:
        d += abs(p[i-1] - p[i])
    else:
        d += p[i]
    
    return d

def swap(p, i, j):
    temp = p[i]
    p[i] = p[j]
    p[j] = temp


def solve(p):
    # Write your code here
    n = len(p)
    # find the present distance
    def get_total_distance(p):
        total_distance = 0
        for i in range(n):
            
            total_distance += get_distance(p, i)
        
        return total_distance

    def position_distance(p, i):
        # left distance + right distance
        # left distance
        left_distance = get_distance(p, i)
        right_distance = get_distance(p, i+1)
        return left_distance + right_distance

    p_distance = [position_distance(p, i) for i in range(n)]
    total_distance = get_total_distance(p)

    minimum_value_so_far = total_distance
    for i in range(n):
        for j in range(i+1, n):
            old_position_distance = p_distance[i] + p_distance[j]
            swap(p, i, j)
            current_position_distance = position_distance(p, i) + position_distance(p, j)
            current_total_distance = total_distance - old_position_distance + current_position_distance
            if current_total_distance < minimum_value_so_far:
                minimum_value_so_far = current_total_distance
            swap(p, i, j)
    return minimum_value_so_far

if __name__ == '__main__':
    a = list(range(1, 6))
    for i in range(6):
        print(solve(a))
        random.shuffle(a)
    print(solve([4, 3, 5, 1, 2]))        

"""
    fptr = open('out.txt', 'w')

    p_count = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = solve(p)

    fptr.write(str(result) + '\n')

    fptr.close()
"""
