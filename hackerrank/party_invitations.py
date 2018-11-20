#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'invitations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY pairs
#

# question is same as number of topological sorts present for a given graph


def invitations(n, pairs):
    # Write your code here

if __name__ == '__main__':
    fptr = open('out.txt', 'w')

    tc = int(input().strip())

    for tc_itr in range(tc):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        pairs = []

        for _ in range(m):
            pairs.append(list(map(int, input().rstrip().split())))

        result = invitations(n, pairs)

        fptr.write(str(result) + '\n')

    fptr.close()