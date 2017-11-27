# http://www.spoj.com/problems/FASHION/

def read_participants():
    value = raw_input()
    return [int(i) for i in value.split(' ')]

def process():
    num_testcases = int(raw_input())
    count = 0
    while count < num_testcases:
        num_participants = int(raw_input())
        men = read_participants()
        women = read_participants()
        men.sort()
        women.sort()
        print sum([x * y for x, y in zip(men, women)])
        count += 1

process()
