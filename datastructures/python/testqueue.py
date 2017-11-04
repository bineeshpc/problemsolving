import queue

q = queue.Queue()

for i in range(10):
    q.enqueue(i), q.isempty()

for i in range(10):
    print q.dequeue(), q.isempty()
