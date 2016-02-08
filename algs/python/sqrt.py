import random

def sqrt(num):
    """
    Given a number returns its square root.
    In this method we iteratively improve our guess.
    As a result of it we get to the solution.
    The guess converges to the solution.
    We use a very small number epsilon.
    
    Args
    num (float or integer): A float or integer.
    Returns
    the square root of the number
    """
    epsilon = 10**-7
    guess = float(num) / 2
    while abs(guess * guess - num) > epsilon:
        print(guess)
        q = num / guess
        guess = (q + guess) / 2
    print("The square root of {} is {}".format(num, guess))
    return guess

print(sqrt(2))
print(sqrt(10))
print(sqrt(25))
print(sqrt(101.19))
