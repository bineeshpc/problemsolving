def dec_to_base(dec, base):
    """
    example with binary, ie base = 2
    20, 2
    
    20 / 2 = 10 remainder 0
    10 / 2 = 5 remainder 0
    5 / 2 = 2 remainder 1
    2 / 2 = 1 remainder 0
    1 / 2 = 0 remainder 1
    
    """
    remainder = dec % base
    divisor = dec / base
    str_remainder = str(remainder)
    if divisor == 0:
        return str_remainder
    else:
        # convert the divisor to the base and append the remainder
        # in the end
        return dec_to_base(divisor, base) + str_remainder

#for i in range(100):
#    print i, dec_to_base(i, 10)


def dec_to_base_iteration(dec, base):
    stack = []
    while (dec != 0):
        divisor = dec / base
        remainder = dec % base
        stack.append(remainder)
        dec = divisor

    value = 0
    while len(stack) > 0:
        out_of_stack = stack.pop()
        value = value * 10 + out_of_stack

    return value
        

print dec_to_base(20, 2)
print dec_to_base_iteration(20, 2)
