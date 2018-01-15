import hashtable
import random

class TestHashtable:
    def setUp(self):
        self.ht = hashtable.Hashtable()
        self.elements = []
   

    def test_insert(self):
        for i in range(2000):
            data = random.randint(1, 10000)
            self.ht.insert(data)
            self.elements.append(data)
            
    def test_search(self):
        for data in self.elements:
            assert self.ht.search(data) == data
            
        for data in range(10001, 20000):
            assert self.ht.search(data) == None

    