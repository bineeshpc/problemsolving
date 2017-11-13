def dec_to_base(dec, base):
    remainder = dec % base
    divisor = dec / base
    str_remainder = str(remainder)
    if divisor == 0:
        return str_remainder
    else:
        return dec_to_base(divisor, base) + str_remainder

for i in range(100):
    print i, dec_to_base(i, 10)
