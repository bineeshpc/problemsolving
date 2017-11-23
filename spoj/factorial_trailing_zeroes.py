# http://www.spoj.com/problems/FCTRL/


def num_divisible(n, a):
    """ Given 2 numbers n and a return
    the number of times n is divisible by a
    """
    count = 0
    remainder = n % a
    if remainder == 0:
        count += 1
        count += num_divisible(n / a, a)
        return count
    else:
        return count

    
def factorial(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * factorial(n-1)


def num_trailing_zeroes_in_factorial(n):
    """ There will be trailing zeroes in n! if and
    only if the numbers involved in it are multiples of 5
    and 2.
    Examples: 5! will have 1 zero because or numbers 5 and 2
    10! will have 2 zeroes because 5, 2, 5, 2. First 5 and 2 were 
    contributed by number 10
    We need to find out the number of times n! is divisible by 5 and 
    number of times n! is divisible by 2
    Let us say that n! is divisible by 5, a times
    and n! is divisible by 2, b times
    Then we take the minimum of a and b
    and that will be the answer
    Take the case of 15!
    5 * 5 * 5, 2 * 2 * 2 * 2 * 2 * 2 * 2
    5 = 3 times
    2 = 7 times
    minimum(3, 7) = 3
    This will have 3 zeroes

    Let us test our theory by writing a simple algorithm for 15!
    Theory seems to be correct!!
    Two count is always greater than 5 counts in a factorial.
    Therefore consider only 5 counts!!
    """
    count1 = n
    five_count = 0
    # two_count = 0
    while count1 >= 1:
        if count1 % 5 != 0:
            count1 -= 1
            continue
        five_count += num_divisible(count1, 5)
        # two_count += num_divisible(count1, 2)
        count1 -= 5
    # min_value = min(five_count, two_count)
    min_value = five_count
    return min_value


def num_trailing_zeroes_in_factorial_efficient(n):
    """ Number of trailing zeroes in n! is
    n / 5 + n / 5^2 + n / 5^3 upto n if 5^k < n
    """
    count = 0
    k = 1
    while True:
        value = n / (5 ** k)
        if value == 0:
            break
        else:
            count += value
        k += 1
    return count

def process():
    num_testcases = int(raw_input())
    count = 0
    while count < num_testcases:
        value = int(raw_input())
        print num_trailing_zeroes_in_factorial_efficient(value)
        count += 1


process()

# for i in range(1, 100):
#     print i, num_divisible(i, 5)
