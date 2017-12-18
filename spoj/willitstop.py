def get_output(n):
    broken = False
    while n > 1:
        if n == 3:
            print "NIE"
            broken = True
            break
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 3
    if not broken:
        print "TAK"

    
n = int(raw_input())
get_output(n)
