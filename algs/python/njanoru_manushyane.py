import sys

filename = './malayalam_string.txt'
with open(filename) as f:
    a = f.read()
    #print len(a.split())
    #sys.stdout.write(a.decode('utf-8'))


#print u'\u0D05'


val = 0xD00
end = 0xD7F
while val != end:
    val += 1
    value = hex(val)[2:]
    value_unicode = '0{}'.format(value)
    # print ord(value_unicode)
    
#print ord(u'\u0D7f')
#print unichr(3333)

for i in range(3333, 3455+1):
    print " ", i, unichr(i), 
