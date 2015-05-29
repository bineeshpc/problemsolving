a = {'a': {'c': {'a': (None, 'aca')}, 'b': {'c': (None, 'abc'), 'd': (None, 'abd')}}, None: {'b': {'d': (None, 'Nbd')}}}

def stringrep(d):
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
        s += strrep + ': ' + stringrep(d[key])
        if num != len(keylist) - 1:
            s += ', '
    s += '}'
    return s

print a
x = stringrep(a)
print x
sorted_a = eval('dict({})'.format(x))
print a == sorted_a

b = {'a': {'b': {'c': (None, 'abc'), 'd': (None, 'abd')}, 'c': {'a': (None, 'aca')}}, None: {'b': {'d': (None, 'Nbd')}}}
print b == sorted_a

y = stringrep(b)
print x == y
