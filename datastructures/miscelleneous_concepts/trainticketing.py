class Train:
    def __init__(self):
        self.seats = [None for _ in range(10)]
        
    def reserveseat(self, seatnumber, customer):
        self.seats[seatnumber] = customer
        print "seat {} reserved for {}".format(seatnumber, customer)

class TicketSystem:
    def __init__(self, train):
        self.train = train
        
    def bookticket(self, customer):
        availableseats = [i for i, s in enumerate(self.train.seats) if s is None]
        print "Available seats are", availableseats
        selectedseat = availableseats.pop(0)
        customer.creditcard.makepayment("trainticketsystem", 100)
        self.sendsms(customer.mobile, 
                     "seat {} reserved for {}".format(selectedseat, customer))
        self.train.reserveseat(selectedseat, customer)
        
    def sendsms(self, mobile, message):
        print "Sending sms to {} Message: {}".format(mobile, message)
        mobile.receivesms(message)

class Person:
    def __init__(self, name, creditcard, mobile):
        self.name = name
        self.creditcard = creditcard
        self.mobile = mobile

class Mobile:
    def __init__(self):
        self.smsstrings = []
    
    def receivesms(self, message):
        self.smsstrings.append(message)

class CreditCard:
    def __init__(self, cardnumber, pin, debt):
        self.cardnumber = cardnumber
        self.pin = pin
        self.debt = debt
        
    def makepayment(self, merchant, amount):
        self.debt += amount

