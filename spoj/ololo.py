
def main():
    counter = dict()
    num_cases = int(raw_input())
    n = num_cases
    unique_num = 0
    while n > 0:
        num = int(raw_input())
        unique_num = unique_num ^ num
        n -= 1
    print unique_num

main()
