"""
Rough and stupid code for calculating electricity bill
of bangalore
"""
t1 = [3.5 for i in range(1,31)]  
t2 =  [4.95 for i in range(31, 101)] 
t3 = [6.5 for i in range(101, 201)]  
t4 = [7.5 for i in range(201, 501)] 
t5 = [8.5 for i in range(501, 10000)] 

tariff = t1 + t2 + t3 + t4 + t5

class ElectricityUsage:
    def __init__(self, units_consumed):
        self.units_consumed = units_consumed
        
    def get_amount(self):
        units_consumed = self.units_consumed
        fixed_charges = 50
        interest = 8.17
        cost = 0
        for unit in range(1, units_consumed+1):
            cost += tariff[unit-1]
        cost += interest
        cost += fixed_charges
        tax = cost * 8.08 / 100
        cost += tax
        
        return cost

previous_reading = 2289
present_reading = 2399
consumption = present_reading - previous_reading
print(ElectricityUsage(consumption).get_amount())
