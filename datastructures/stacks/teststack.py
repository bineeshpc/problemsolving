import stack

s = stack.Stack()

for i in range(10):
    s.push(i)
    print s

for i in range(10):
    print s.pop()
    print s

