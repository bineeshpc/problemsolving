def string_match(str_1, pattern):
    pattern_length = len(pattern)
    str_length = len(str_1)
    for i in range(str_length):
        stri = i
        patterni = 0
        while patterni < pattern_length and stri < str_length and str_1[stri] == pattern[patterni]:
            stri += 1
            patterni += 1
        if patterni == pattern_length:
            return i
    return -1

print string_match('paneerbuttermasala', 'masala1')
