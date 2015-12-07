a = []
for i in range(10**100):
    a.append(i)
    if i % 10**5 == 0:
        print(i)