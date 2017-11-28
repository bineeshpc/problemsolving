# http://www.spoj.com/problems/JULKA/


def get_output(total_apples, g1_more):
    # total_apples x + y
    # g1_more  x - y
    x = (total_apples + g1_more) / 2
    y = total_apples - x
    print x
    print y

def process():
    count = 0
    while count < 10:
        total_apples = int(raw_input())
        g1_more = int(raw_input())
        get_output(total_apples, g1_more)
        count += 1


process()
