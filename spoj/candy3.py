# http://www.spoj.com/problems/CANDY3/


def process():
    num_cases = int(input())
    count = 0
    

    while count < num_cases:
        blank = input()
        num_students = int(input())
        count_students = 0
        sum1 = 0
        while count_students < num_students:
            sum1 += int(input())
            count_students += 1
        if sum1 % count_students == 0:
            print("YES")
        else:
            print("NO")
        count += 1

process()
