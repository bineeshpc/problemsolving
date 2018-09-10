import six

def digital_root(num):
    """ digital root of a number is found by  
    the summing up all elements until we get a single
    digit number 
    1729   -> 19 -> 10 -> 1 (returns 1)
    """
    
    def digital_sum(num):
        if num < 10:
            return num
        else:
            last_digit = num % 10
            remaining_number = num // 10
            return last_digit + digital_sum(remaining_number)
    
    if num < 10:
        return num
    else:
        digsum = digital_sum(num)
        return digital_root(digsum)


six.print_(digital_root(10**20-1))