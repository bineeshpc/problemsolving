# http://www.spoj.com/problems/EIGHTS/
def get_num(k):
    x = (k - 1) / 4
    y = (k - 1) % 4
    vals = [192, 442, 692, 942]
    return x * 1000 + vals[y]
    

def process():
    n = int(raw_input())
    for _ in range(n):
        k = int(raw_input())
        print get_num(k)


process()
