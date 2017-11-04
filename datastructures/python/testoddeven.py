import oddeven
import threading

def test_oddeven():
    t1 = oddeven.OddEven(1)
    t2 = oddeven.OddEven(2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def test_oddeven1():
    t1 = oddeven.Odd()
    t2 = oddeven.Even()
    t1.start()
    t2.start()
    t1.join()
    t2.join()  