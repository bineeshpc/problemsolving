first_round = "TFMRL"
second_round = "RMFTFMRL"

def count(n):
    if n <= 5:
        return first_round[n-1]
    else:
        return second_round[(n-5) % 8 - 1]

for i in range(1, 1000):
    print i, count(i)