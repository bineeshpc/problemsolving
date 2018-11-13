binary_digits = [str(i) for i in range(2)]

def get_all_binaries_of_length_n(n):
    #print "..." * (N - n), 'print_binary({})'.format(n)
    if n == 0:
        return [""]
    else:
        lst = get_all_binaries_of_length_n(n-1)
        lst1 = []

        for digit in binary_digits:
            for x in lst:
                lst1.append(digit + x)
                
        return lst1


    
N = 3
n = N
print()
#print get_all_binaries_of_length_n(n)


binary_digits = [[i] for i in range(2)]

def get_all_binaries_of_length_n_lst(n):
    #print "..." * (N - n), 'print_binary({})'.format(n)
    if n == 0:
        return [[]]
    else:
        lst = get_all_binaries_of_length_n_lst(n-1)
        lst1 = []

        for digit in binary_digits:
            for x in lst:
                lst1.append(digit + x)
                
        return lst1

    
N = 3
n = N
print()
print(get_all_binaries_of_length_n_lst(n))
