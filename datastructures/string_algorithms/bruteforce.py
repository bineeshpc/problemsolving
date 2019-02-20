def string_match(pattern, txt):
    """ String match brute force
    """
    pattern_length = len(pattern)
    txt_length = len(txt)
    for i in range(txt_length):
        txti = i
        patterni = 0
        while (patterni < pattern_length) and (txti < txt_length) and (txt[txti] == pattern[patterni]):
            txti += 1
            patterni += 1
        if patterni == pattern_length:
            return i
    return -1

