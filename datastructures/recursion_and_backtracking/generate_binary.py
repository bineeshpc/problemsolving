

def get_all_binaries_of_length_n(n):
    #print "..." * (N - n), 'print_binary({})'.format(n)
    if n == 0:
        return [""]
    else:
        lst = get_all_binaries_of_length_n(n-1)

        lst1 = []
        for x in lst:
            lst1.append("0" + x)
        for x in lst:
            lst1.append("1" + x)

        return lst1

    
N = 5
n = N
print
print get_all_binaries_of_length_n(n)
