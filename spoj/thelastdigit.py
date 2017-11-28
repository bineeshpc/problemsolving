prind1 = {
    2 :[2, 4, 8, 6],
    3 :[3, 9, 7, 1],
    4 : [4, 6],
    7 : [7, 9, 3, 1],
    8 : [8, 4, 2, 6],
    9: [9, 1]
}
d2 = {
    2 : 4,
    3 : 4,
    4 : 2,
    7 : 4, 
    8 : 4, 
    9: 2
}
def ld(a, b):
    l = a % 10
    if b == 0:
        return 1
    if l == 0:
        return 0
    if l == 1 or l == 5 or l == 6:
        return l
    if l == 2 or l == 3 or l == 4 or l == 7 or l == 8 or l == 9:
        x = d2[l]
        return d1[l][(b - 1) % x]

r = raw_input
    
def p():
    n = int(r())
    c = 0
    while c < n:
        x = r()
        a, b = map(int, x.split(' '))
        print ld(a, b)
        c += 1

p()
