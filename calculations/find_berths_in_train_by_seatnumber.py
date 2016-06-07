"""
Prints a list of Upper births and side upper births in 
Indian railways
"""
def upper_berth_rule(x):
    return x==3 or x==6

def side_upper_rule(x):
    return x == 7

def is_condition(seat_number, function):
    x = seat_number % 8
    return function(x)
    
def is_upper_berth(seat_number):
    return is_condition(seat_number, upper_berth_rule)

def is_side_upper(seat_number):
    return is_condition(seat_number, side_upper_rule)
    

print 'Upper births',  [i for i in range(1, 73) if is_upper_berth(i) == True]
print 'Side Upper births', [i for i in range(1, 73) if is_side_upper(i) == True] 
