import linkedlist

class Hashtable:
    def __init__(self, size=1000):
        self.size = size
        self.array = [None for i in range(self.size)]

    def hash(self, data):
        return data % self.size
        
    def insert(self, data):
        key = self.hash(data)
        if self.array[key] != None:
            self.array[key].insert(data)
        else:
            lst = linkedlist.List()
            lst.insert(data)
            self.array[key] = lst

    def search(self, data):
        key = self.hash(data)
        if self.array[key]:
            self.array[key].search(data)
            
    