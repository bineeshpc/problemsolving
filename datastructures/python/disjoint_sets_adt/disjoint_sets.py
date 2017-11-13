class Disjoint_sets1(object):
    """ Fast union implementation
    Find is slow in this implementation"""
    def __init__(self):
        pass

    def make_set(self, n):
        """ All elements are numbered from 1 to n-1
        Name of the set is in stored in the location indexed by the element
        Args: n which is an ingeger
        Returns: None
        """
        self.data = [i for i in range(n)]

    def find(self, n):
        """ Finds the set name of given element 
        Complexity is the size of the set """
        try:
            if self.data[n] == n:
                return n
            else:
                return self.find(self.data[n])
        except KeyError:
            return None

    def union(self, root1, root2):
        """ union of 2 sets is O(1)"""
        self.data[root1] = root2

    def get_all_setnames(self):
        setnames = {}
        for i in self.data:
            setnames[i] = True
        return setnames.keys()

    def cardinality_of_set(self, setname):
        """ Given a setname find its cardinality """
        count = 0
        for i in self.data:
            if i == setname:
                count += 1
        return count

ds = Disjoint_sets1()
ds.make_set(20)
print ds.find(4)
print ds.find(5)

ds.union(4, 5)
ds.union(6, 5)

print ds.find(4)
print ds.find(5)
print ds.find(6)

print ds.get_all_setnames()
print ds.cardinality_of_set(1)
print ds.cardinality_of_set(5)
