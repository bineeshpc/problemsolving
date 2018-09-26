import sys
import testlib

def compareto(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

class BinarySearchST:
    def __init__(self):
        self.keys = []
        self.values = []
        self.n = 0

    def put(self, key, value):
        if value == None:
            self.delete(key)
            return
        rank = self.rank(key)
        if rank >= 0 and rank < self.size() and self.keys[rank] == key:
            # easy case when key is already present
            # fast operation
            self.values[rank] = value
            return

        # when key is not present we need to move all the existing keys
        # after the rank to right 
        # and insert the key at the right position
        self.keys.append(key)   # dummy insert just to change size
        self.values.append(value) # dummy insert just to change size

        # dummy insert positions will be overwritten by 
        # the below loop
        # move all keys and values by one place
        
        i = self.size() - 2
        while i > rank:
            self.keys[i+1] = self.keys[i]
            self.values[i+1] = self.values[i]
            i -= 1
        # insert the key and value in right place
        self.keys[rank] = key
        self.values[rank] = value
        self.n += 1


    def get(self, key):
        rank = self.rank(key)
        if rank >= 0 and rank < self.size() and self.keys[rank] == key:
            return self.values[rank]
        else:
            return None
                
    def contains(self, key):
        if self.get(key) != None:
            return True
        return False
        
    def __iter__(self):
        self.iterhelper = 0
        return self
        
    def __next__(self):
        if self.iterhelper < self.size():
            i = self.iterhelper
            self.iterhelper += 1
            return (self.keys[i], self.values[i])
        else:
            raise StopIteration

    def size(self):
        return self.n

    def isempty(self):
        return self.size() == 0

    def delete(self, key):
        rank = self.rank(key)
        if self.keys[rank] == key:
            # key is present delete it
            del self.keys[rank]
            del self.values[rank]
            self.n -= 1
            

    def min(self):
        if self.isempty():
            raise Exception('called min() on empty symbol table')
        return self.keys[0]

    def max(self):
        if self.isempty():
            raise Exception('called max() on empty symbol table')
        return self.keys[self.size() - 1]

    def select(self, key):
        if key < 0 or key > (self.size() - 1):
            raise Exception('K should be between 0 and {}'.format(self.size()-1))
        return self.keys[key]

    def rank(self, key):
        low = 0
        high = self.size() - 1
        while low <= high:
            mid = low + (high - low) // 2
            cmp = compareto(key, self.keys[mid])
            if cmp < 0:
                high = mid - 1
            elif cmp > 0:
                low = mid + 1
            else:
                return mid
        return low

def main():
    st = BinarySearchST()
    testlib.test_BinarySearchST(st)

if __name__ == '__main__':
    main()