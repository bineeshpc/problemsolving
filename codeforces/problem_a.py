
def read_input():
    n = int(input())
    s2 = input()
    a = [int(i) for i in s2.split()]
    return n, a


def problem_a(n, a):
    """ Find largest streak of largest element
    """
    largest = max(a)
    i = 0
    old_streak_begin = 0
    old_streak_end = 0
    while i < n:
        if a[i] == largest:
            streak_begin = i
            while i < n and a[i] == largest:
                i += 1
            streak_end = i - 1
            i -= 1 # adjust index back
            if (streak_end - streak_begin) < (old_streak_end - old_streak_begin):
                streak_begin = old_streak_begin
                streak_end = old_streak_end
            else:
                old_streak_begin = streak_begin
                old_streak_end = streak_end
        
        i += 1
    
    print(streak_end - streak_begin + 1)



if __name__ == '__main__':
    n, a = read_input()
    problem_a(n, a)