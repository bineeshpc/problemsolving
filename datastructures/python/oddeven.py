import threading
import time

class OddEven(threading.Thread):
    def __init__(self, begin):
        threading.Thread.__init__(self)
        self.begin = begin
        
    def run(self):
        var = self.begin
        while True:
            print var
            time.sleep(.5)
            var = var + 2
            if var > 100:
                break

number = 1
           
class Odd(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        global number
        while True:
            if number % 2 == 1:
                print number, self.name
                number = number + 1
            time.sleep(.5)
            if number > 100:
                break
            
class Even(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        global number
        while True:
            if number % 2 == 0:
                print number, self.name
                number = number + 1
            time.sleep(.5)
            if number > 100:
                break