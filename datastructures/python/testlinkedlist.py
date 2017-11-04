import linkedlist
import random


def testcreatelist():
    lst = range(25,35)
    lst1 = linkedlist.List()
    lst1.createlist(lst)
    print lst1
    assert lst1.tolist() == lst

def testdelete():
    lst = range(25, 35)
    lst1 = linkedlist.List()
    lst1.createlist(lst)
    for i in range(5):
        x = random.choice(range(25, 45))
        lst1.delete(x)
        try:
            lst.remove(x)
        except ValueError:
            pass
        assert lst1.tolist() == lst
    print lst1

def testnocycle():
    lst = linkedlist.List()
    for i in range(10):
        lst.insert(i)
    print lst
    lst.detectcycle() == False

def test_cycle():
    cyclelist = linkedlist.List()
    cyclelist.createcycle(5, 6)
    assert cyclelist.detectcycle() == True

def testsearch():
    lst = range(25,35)
    lst1 = linkedlist.List()
    lst1.createlist(lst)
    print lst1
    assert lst1.search(26) == 26
    assert lst1.search(50) == None   