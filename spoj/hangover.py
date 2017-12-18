# http://www.spoj.com/problems/HANGOVER/

def hangover(n):
    """ 1/2 + 1/3... 1/n+1 """
    return sum([1.0 / (i + 2) for i in range(n)])

# print hangover(1.0)

def num_cards_required(n):
    count = 1
    while True:
        if hangover(count) > n:
            break
        count += 1
    return count


def process():
    epsilon = 0.00000001
    while True:
        n = float(raw_input())
        if n - 0.0 < epsilon:
            break
        else:
            print num_cards_required(n), 'card(s)'
        

process()
