def process():
    num_cases = int(raw_input())
    count = 0


    while count < num_cases:
        broken = False
        x = raw_input()
        num_stamps, num_friends = map(int, x.split())
        y = raw_input()
        friends = map(int, y.split())
        friends.sort(reverse=True)
        sum1 = 0
        for n, friend in enumerate(friends):
            sum1 += friend
            if sum1 >= num_stamps:
                broken = True
                break
        print "Scenario #{}:".format(count + 1)
        if broken:
            print n + 1
        else:
            print "impossible"
        print
        count += 1

process()
