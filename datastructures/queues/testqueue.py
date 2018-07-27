import queue

qarray = queue.Queue()
qlist = queue.QueueList()

def test_queue(q):
    for i in range(1, 11):
        q.enqueue(i), q.isempty()

    for i in range(1, 11):
        print q.dequeue(), q.isempty()

test_queue(qarray)
test_queue(qlist)
