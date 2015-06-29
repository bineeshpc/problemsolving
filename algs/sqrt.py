def sqrt(num):
    guess = float(num) / 2
    while abs(guess * guess - num) > .0000001:
        print(guess)
        q = num / guess
        guess = (q + guess) / 2
    return guess

print(sqrt(2))
print(sqrt(10))
print(sqrt(25))
