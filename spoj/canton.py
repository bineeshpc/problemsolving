import math

def find_row_number(x):
    n = int(math.sqrt(2 * x))
    def f(n):
        return n * (n+1) / 2
    while True:
        if f(n-1) <= x and x <= f(n):
            first_one = f(n-1) + 1
            return n, first_one
        # print n
        n += 1


def get_answer(n):
    if n == 1:
        numerator, denominator = 1, 1
    elif n == 2:
        numerator, denominator = 1, 2
    elif n == 3:
        numerator, denominator = 2, 1
    else:
        row_number, first_one  = find_row_number(n)
        index = n - first_one
        y = row_number + 1
        if row_number % 2 == 1:
            # row = [(y-i, i) for i in range(1, y)]
            a = (y - index - 1, index + 1)
        else:
            # row = [(i, y-i) for i in range(1, y)]
            a = (index + 1, y - index - 1)
        
        numerator, denominator = a  # row[index]
        # print a
    return "TERM {} IS {}/{}".format(n, numerator, denominator)            

    
    
def process():
    n = int(raw_input())
    for _ in range(n):
        x = int(raw_input())
        print get_answer(x)

process()


