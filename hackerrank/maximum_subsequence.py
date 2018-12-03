# https://www.hackerrank.com/challenges/common-child/
import sys

sys.setrecursionlimit(10000)

def longest_subsequence_length1(s1, s2):
    cache = {}
    def longest_subsequence_length_helper(s1, s2, cache):
        if (s1, s2) in cache:
            return cache[(s1, s2)]
        s1_length = len(s1)
        s2_length = len(s2)
        if s1_length == 0 or s2_length == 0:
            cache[(s1, s2)] = 0
            return cache[(s1, s2)]

        first = s1[0:s1_length-1]
        second = s2[0:s2_length-1]
        f = s1[s1_length-1]
        s = s2[s2_length-1]
        if f == s:
            cache[(s1, s2)] = 1 + longest_subsequence_length_helper(first, second, cache)
            return cache[(s1, s2)]
        else:
            c1 = longest_subsequence_length_helper(first, second, cache)
            c2 = longest_subsequence_length_helper(s1, second, cache)
            c3 = longest_subsequence_length_helper(first, s2, cache)
            cache[(s1, s2)] = max(c1, c2, c3)
            return cache[(s1, s2)]

    return longest_subsequence_length_helper(s1, s2, cache)

def longest_subsequence_length2(s1, s2):
    cache = {}
    def longest_subsequence_length_helper(s1, s2, m, n, cache):
        if m == -1 or n == -1:
            return 0

        if (m, n) in cache:
            return cache[(m, n)]

        if s1[m] == s2[n]:
            cache[(m, n)] = 1 + longest_subsequence_length_helper(s1, s2, m-1, n-1, cache)
            return cache[(m, n)]
        else:
            c1 = longest_subsequence_length_helper(s1, s2, m-1, n-1, cache)
            c2 = longest_subsequence_length_helper(s1, s2, m-1, n, cache)
            c3 = longest_subsequence_length_helper(s1, s2, m, n-1, cache)
            cache[(m, n)] = max(c1, c2, c3)
            return cache[(m, n)]
    
    return longest_subsequence_length_helper(s1, s2, len(s1)-1, len(s2)-1, cache)

def longest_subsequence_length(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)
    cache = []
    for i in range(s1_length+1):
        cache.append([])
        for j in range(s2_length+1):
            cache[i].append(0)

    for i in range(s1_length):
        for j in range(s2_length):
            if s1[i] == s2[j]:
                cache[i+1][j+1] = cache[i][j] + 1
            elif cache[i+1][j] > cache[i][j+1]:
                cache[i+1][j+1] = cache[i+1][j]
            else:
                cache[i+1][j+1] = cache[i][j+1]
    return cache[s1_length][s2_length]

def main():
    t = int(input())
    for _ in range(t):
        s1 = input()
        s2 = input()
        print(longest_subsequence_length(s1, s2))

if __name__ == "__main__":
    main()