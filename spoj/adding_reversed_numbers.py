# http://www.spoj.com/problems/ADDREV/


def reverse_number(number, base):
    value = 0
    first_non_zero_found = False
    while number != 0:
        remainder = number % base
        quotient = number / base
        if remainder == 0 and not first_non_zero_found:
            number = quotient
        else:
            first_non_zero_found = True
            number = quotient
            value *= base
            value += remainder
    return value

def add_reverse_and_reverse(first_num, second_num):
    first_reversed = reverse_number(first_num, 10)
    second_reversed = reverse_number(second_num, 10)
    reversed_number = reverse_number(first_reversed + second_reversed, base)
    return reversed_number

num_testcases = int(raw_input())
count = 0
while count < num_testcases:
    value = raw_input()
    first, second = value.split(' ')
    first = int(first)
    second = int(second)
    print add_reverse_and_reverse(first, second)
    count += 1
