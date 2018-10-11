"""
Prints a list of Upper births and side upper births in 
Indian railways
"""
def upper_berth_rule(x):
    return x == 2 or x == 5

def side_upper_rule(x):
    return x == 7

def lower_berth_rule(x):
    return x == 0 or x == 3

def side_lower_rule(x):
    return x == 6

def middle_berth_rule(x):
    return x == 1 or x == 4

def is_condition(seat_number, function):
    x = (seat_number - 1) % 8
    return function(x)
    
def is_upper_berth(seat_number):
    return is_condition(seat_number, upper_berth_rule)

def is_side_upper(seat_number):
    return is_condition(seat_number, side_upper_rule)
    
def is_lower_berth(seat_number):
    return is_condition(seat_number, lower_berth_rule)

def is_side_lower(seat_number):
    return is_condition(seat_number, side_lower_rule)

def is_middle_berth(seat_number):
    return is_condition(seat_number, middle_berth_rule)


print('Upper births',  [i for i in range(1, 73) if is_upper_berth(i) == True])
print('Middle births', [i for i in range(1, 73) if is_middle_berth(i) == True]) 
print('Lower births', [i for i in range(1, 73) if is_lower_berth(i) == True]) 
print('Side Upper births', [i for i in range(1, 73) if is_side_upper(i) == True]) 
print('Side Lower births', [i for i in range(1, 73) if is_side_lower(i) == True]) 
