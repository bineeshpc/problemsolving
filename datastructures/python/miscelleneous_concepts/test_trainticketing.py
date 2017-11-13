import trainticketing

    
class TestTicketing:
    def setUp(self):
        self.train = trainticketing.Train()
        cc = trainticketing.CreditCard(1234, 56, 0)
        mobile = trainticketing.Mobile()
        self.customer = trainticketing.Person("Bini", cc, mobile)
        self.system = trainticketing.TicketSystem(self.train)
    
    def testbookticket(self):
        self.system.bookticket(self.customer)