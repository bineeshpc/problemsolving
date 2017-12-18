# http://www.spoj.com/problems/COINS/
import math

change_coins_stored = {}

def change_coins(n):
    if change_coins_stored.has_key(n):
        return change_coins_stored[n]
    else:
        a = n / 2
        b = n / 3
        c = n / 4
        if n >= a + b + c:
            change_coins_stored[n] = n
            return n
        else:
            x = change_coins(a)
            y = change_coins(b)
            z = change_coins(c)
            sum1 = x + y + z
            change_coins_stored[n] = sum1
            return sum1

def process():
    for _ in range(10):
        try:
            n = int(raw_input())
            print change_coins(n)
        except:
            break

process()
