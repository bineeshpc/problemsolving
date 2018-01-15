"""
circle inside a square.
pi * r**2 
(2r) ** 2 = 4r**2
when r = 1
cirle = pi
square = 4
random shoots of points.
hits/total = pi/4
pi = 4 * hits/total 

"""

import random
from threading import Thread
from multiprocessing import Process, Queue

def is_insidecircle(x, y):
    if x ** 2 + y ** 2 <= 1:
        return True
    else:
        return False
a = []
b = []

def runsimulation(samplesize, q):
    hits = 0.0
    global a, b
    for _ in range(samplesize):
        x, y = [random.uniform(-1, 1) for i in range(2)]
        if is_insidecircle(x, y):
            hits += 1
    print hits, samplesize
    q.put((hits, samplesize))

size = 10**8
numthreads = 10
samplesize = size/numthreads
q = Queue()
for _ in range(numthreads):
    p = Process(target=runsimulation, args=(samplesize, q))
    p.start()


for _ in range(numthreads):
    x, y = q.get()
    a.append(x)
    b.append(y)


    
#     t = Thread(target=runsimulation, args=(samplesize,))
#     t.start()
#     t.join()

#print 4 * hits / samplesize, samplesize
print 4*sum(a)/sum(b)

#for s in range(10 ** 6, 10 ** 7, 10 ** 6):
    #runsimulation(s)
#runsimulation(10**8)
