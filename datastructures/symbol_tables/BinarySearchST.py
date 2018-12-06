import sys
import testlib

def compare_to(a, b):
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
            
    def floor(self, key):
        """
        Returns the largest element less than or equal to given key
        """
        rank = self.rank(key)
        if rank < self.size() and compare_to(key, self.keys[rank]) == 0:
            return self.keys[rank]
        if rank - 1 >= 0:
            return self.keys[rank-1]
        else:
            return None

    def ceiling(self, key):
        """
        Returns the smallest element greater than or equal to given key
        """
        rank = self.rank(key)
        if rank < self.size() and compare_to(key, self.keys[rank]) == 0:
            return self.keys[rank]

        if rank + 1 <= self.size() - 1:
            return self.keys[rank+1]
        else:
            return None

    def min(self):
        if self.isempty():
            raise Exception('called min() on empty symbol table')
        return self.keys[0]

    def max(self):
        if self.isempty():
            raise Exception('called max() on empty symbol table')
        return self.keys[self.size() - 1]

    def delete_min(self):
        if self.isempty():
            raise Exception('called delete min on empty symbol table')
        self.delete(self.min())


    def delete_max(self):
        if self.isempty():
            raise Exception('called delete min on empty symbol table')
        self.delete(self.max())


    def select(self, k):
        """
        kth order statistic
        return the kth smallest element
        """
        if k < 0 or k > (self.size() - 1):
            raise Exception('K should be between 0 and {}'.format(self.size()-1))
        return self.keys[k]

    def rank(self, key):
        """
        Returns the rank of the element 
        ie if key is present then return its position
        if key is not present return the position where it will be inserted
        """
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

    # internal invariants are given below

    def is_sorted(self):
        for i in range(1, self.size()):
            if self.keys[i-1] > self.keys[i]:
                return False
        return True

    def rank_check(self):
        for i in range(self.size()):
            # select the ith element
            # and compute its rank
            # rank of ith key is going to be i
            if self.rank(self.select(i)) != i:
                return False
            # compute the rank of each key

            if self.keys[i] != self.select(self.rank(self.keys[i])):
                return False
        return True



    def check(self):
        return self.is_sorted() and self.rank_check()

def main():
    st = BinarySearchST()
    testlib.test_BinarySearchST(st)

if __name__ == '__main__':
    main()