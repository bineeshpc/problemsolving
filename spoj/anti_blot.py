def cleanup(a, b):
    if a.find(b) == -1:
        return int(a)
    else:
        return None

def get_answer(str1):
    problem, answer = str1.split('=')
    f, s = problem.split('+')
    b = 'machula'
    f = cleanup(f, b)
    s = cleanup(s, b)
    answer = cleanup(answer, b)

    if f is None:
        f = answer - s
    elif s is None:
        s = answer - f
    elif answer is None:
        answer = s + f
        
    return "{} + {} = {}".format(f, s, answer)

def process():
    n = int(raw_input())
    for _ in range(n):
        raw_input()  # blank line
        str1 = raw_input()
        print get_answer(str1)

process()
