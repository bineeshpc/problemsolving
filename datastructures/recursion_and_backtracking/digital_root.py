def digital_root(num):
    """ digital root of a number is found by  
    the summing up all elements until we get a single
    digit number 
    1729   -> 19 -> 10 -> 1 (returns 1)
    """
    def digital_sum(num):
        # basecase number is 0
        if num == 0:
            return num
        # recursive case
        else:
            last_digit = num % 10
            remaining_number = num / 10
            return last_digit + digital_sum(remaining_number)

    # base case
    if num < 10:
        return num
    # recursive case
    else:
        return digital_root(digital_sum(num))


print digital_root(123456)
        
    
