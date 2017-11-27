# http://www.spoj.com/problems/CANDY3/

def get_answer(all_candies, length1):
    sum1 = 0
    for i in all_candies:
        x = int(i / length1)
        print(x)
        sum1 += i
    return (sum1 % length1) == 0


def process():
    num_cases = int(input())
    count = 0
    all_candies = []
    length1 = 0
    eof = False
    while(count < num_cases+1):
        try:
            candies = input()
        except EOFError:
            eof = True
        if candies == '' or eof:
            count += 1
            #  print(all_candies, length1)
            if length1 != 0:
                if get_answer(all_candies, length1):
                    print("YES")
                else:
                    print("NO")
                all_candies = []
                length1 = 0
        else:
            num_candies = int(candies)
            all_candies.append(num_candies)
            length1 += 1
        

process()
