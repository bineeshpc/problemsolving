import sys
import random

INFINITY = sys.maxint

def get_matices(values):
    matrices = []
    n = len(values)
    matrices.append(values[0])
    for i in range(1, n-1):
        matrices.append(values[i])
        matrices.append(values[i])
    matrices.append(values[len(values)-1])
    index = 0
    tuples = []
    while index < len(matrices):
        first = matrices[index]
        second = matrices[index+1]
        tuples.append((first, second))
        index += 2
        
    return tuples

def optimal_paranthesization(a):
    def optimal_paranthesization_helper(a, start, end):
        if start == end:
            return 0
        else:
            cost = INFINITY
            for i in range(start, end):
                first_segment_cost = optimal_paranthesization_helper(a, start, i)
                second_segment_cost = optimal_paranthesization_helper(a, i+1, end)
                cost_of_multication = a[start][0] * a[i][1] * a[end][1]   # rows of first segment * columns of first segment * columns of second segment
                
                if first_segment_cost + second_segment_cost + cost_of_multication < cost:
                    cost = first_segment_cost + second_segment_cost + cost_of_multication
            return cost

    return optimal_paranthesization_helper(a, 0, len(a)-1)

def optimal_paranthesization_memoization(a):
    cache = {}
    def optimal_paranthesization_helper(a, start, end):
        if start == end:
            return 0
        else:
            if cache.get((start, end)):
                return cache[(start, end)]
            else:
                cost = INFINITY
                for i in range(start, end):
                    first_segment_cost = optimal_paranthesization_helper(a, start, i)
                    second_segment_cost = optimal_paranthesization_helper(a, i+1, end)
                    cost_of_multication = a[start][0] * a[i][1] * a[end][1]   # rows of first segment * columns of first segment * columns of second segment

                    if first_segment_cost + second_segment_cost + cost_of_multication < cost:
                        cost = first_segment_cost + second_segment_cost + cost_of_multication
                cache[(start, end)] = cost
                return cache[(start, end)]

    return optimal_paranthesization_helper(a, 0, len(a)-1)


def optimal_paranthesization_tabulation(a):
    """
    Start by computing optimal paranthesization for 1 matrix, 2 matrices, 3 matrices and so on until we reach our desired solution
    """

example = [random.randint(10, 100) for i in range(17)]
example = get_matices(example)
print example
import time
begin = time.time()
print optimal_paranthesization(example)
end = time.time()
print end - begin
begin = time.time()
print optimal_paranthesization_memoization(example)
end = time.time()
print end - begin
