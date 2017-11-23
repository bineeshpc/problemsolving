# http://www.spoj.com/problems/PRIME1/

import math


unmarked = 0
marked = 1


def is_prime(n):
    if n == 0 or n == 1:
        return False
    n_sqrt = math.sqrt(n)
    num = int(math.floor(n_sqrt))
    count = 2
    while count <= num:
        remainder = n % count
        if remainder == 0:
            return False
        count += 1
    return True

def simple_sieve(n):
    """ returns all primes below n """
    length_of_sieve = n+1
    sieve = [unmarked for _ in range(2, length_of_sieve)]  # sieve represented as an array of numbers
    # index of the sieve crepresents the number 
    unmarked_number = 2  # we start from 2 the smallest prime number
    last_number_in_sieve = length_of_sieve - 1
    # for all unmarked numbers in sieve
    # mark the multiples of unmarked numbers in sieve until 
    # we reach the end of the sieve
    while unmarked_number <= last_number_in_sieve:
        # print "unmarked number", unmarked_number, last_number_in_sieve
        # print sieve
        if sieve[unmarked_number - 2] == unmarked:
            scalar = 2
            while True:  # code to mark all the multiples of an unmarked number to marked
                multiple = scalar * unmarked_number
                if multiple > last_number_in_sieve:
                    break
                # print multiple, last_number_in_sieve
                sieve[multiple - 2] = marked
                scalar += 1
        unmarked_number += 1
    return sieve


def get_primes_below_n(n):
        simple_sieve_array = simple_sieve(n)
        prime_numbers = []
        length = len(simple_sieve_array)
        for i in range(2, length + 2):
            if simple_sieve_array[i-2] == unmarked:
                prime_numbers.append(i)
        return prime_numbers


def do_segmented_sieve(begin, end):
    sieve_size = int(math.sqrt(end))
    primes = get_primes_below_n(sieve_size)
    # print primes
    # print sieve_size, len(primes), primes
    def mark_all_in_sieve(sieve, begin, end, prime):
        multiplier = begin / prime
        while True:
            multiple = multiplier * prime
            
            # print multiple, begin, multiple - begin, end
            if multiple >= begin and multiple <= end:
                sieve[multiple-begin] = marked
            elif multiple > end:
                break
            multiplier += 1

    def process_single_sieve(sieve_size, begin, primes):
        sieve = [unmarked for _ in range(sieve_size)]
        # print sieve, primes, sieve_size
            
        for prime in primes:
            # print prime
            if begin+sieve_size < end + sieve_size:
                mark_all_in_sieve(sieve, begin, begin+sieve_size-1, prime)
        # print sieve
        for i in range(sieve_size):
            number = begin + i
            if sieve[i] == unmarked and number <= end:
                print number
    try:
        if begin <= primes[-1]:
            for prime in primes:
                if prime >= begin and prime <= end:
                    print prime
            begin = primes[-1] + 1
    except IndexError:
        pass
    for n in range(begin, end, sieve_size):
        # print n, sieve_size
        process_single_sieve(sieve_size, n, primes)


def process():
    num_testcases = int(raw_input())
    count = 0
    while count < num_testcases:
        value = raw_input()
        begin, end = value.split(' ')
        begin = int(begin)
        end = int(end)
        if begin <= 5 or end <= 5:
            num = begin
            while num <= end:
                if is_prime(num):
                    print num
                num += 1
        else:
            do_segmented_sieve(begin, end)
        print
        count += 1


process()

