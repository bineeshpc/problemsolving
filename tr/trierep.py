

class Trie:

    def __init__(self, trie):
        self.trie = trie

    def stringrep(self, d):
        try:
            keylist = d.keys()
            keylist.sort()
        except AttributeError:
            return '{}'.format(d)
        s = '{'
        for num, key in enumerate(keylist):
            if isinstance(key, basestring):
                strrep = "'{}'".format(key)
            else:
                strrep = str(key)
            s += strrep + ': ' + self.stringrep(d[key])
            if num != len(keylist) - 1:
                s += ', '
        s += '}'
        return s


a = {'a': {'c': {'a': (None, 'aca')}, 'b': {'c': (None, 'abc'), 'd': (None, 'abd')}}, None: {'b': {'d': (None, 'Nbd')}}}
print a
t = Trie(a)
x = t.stringrep(a)
print x
sorted_a = eval('dict({})'.format(x))
print a == sorted_a

b = {'a': {'b': {'c': (None, 'abc'), 'd': (None, 'abd')}, 'c': {'a': (None, 'aca')}}, None: {'b': {'d': (None, 'Nbd')}}}
print b == sorted_a

t1 = Trie(b)
y = t1.stringrep(b)
print x == y
