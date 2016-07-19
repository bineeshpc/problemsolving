"""
29 * x + 30 * y + 31 * z = 366
"""
from itertools import product as p

def is_366(x, y, z):
    return 29 * x + 30 * y + 31 * z == 366
    
for x, y, z in p(range(0, 12), repeat=3):
    is_sol = is_366(x, y, z)
    if is_sol:
        print x, y, z
