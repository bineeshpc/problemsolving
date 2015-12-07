import random

filename = '/mnt/testing/mergesort_input.txt'
largestnumber = 400 * 10 ** 6
with open(filename, 'w') as f:
    for i in range(200 * 10 ** 6):
        randomnumber = random.randint(1, largestnumber)
        f.write('{}\n'.format(randomnumber))