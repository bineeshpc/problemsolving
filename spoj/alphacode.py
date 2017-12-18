# http://www.spoj.com/problems/ACODE/

import string

alpha_number = {v: k+1 for k, v in enumerate(string.uppercase)}
number_alpha = [v for v in string.uppercase]
valid_codes = {}

def get_number(alpha):
    return alpha_number[alpha]

def get_alpha(number):
    return number_alpha[number - 1]

def get_valid_codes1(str1):
    if str1 in valid_codes:
        return valid_codes[str1]
    length = len(str1)
    candidates = []
    for i in range(length):
        candidate1 = int(str1[i])
        candidates.append((candidate1, str1[i+1:]))
        if i+2 <= length:
            candidate2 = int(str1[i:i+2])
            if candidate2 <= 26:
                candidates.append((candidate2, str1[i+2:]))
    valid_codes[str1] = candidates
    return candidates

def get_valid_codes(str1):
    if str1 in valid_codes:
        return valid_codes[str1]
    candidates = []
    candidate1 = str1[0]
    candidate1 = int(candidate1)
    candidates.append((candidate1, str1[1:]))
    candidate2 = str1[0:2]
    candidate2 = int(candidate2)
    if candidate2 != candidate1:
        candidates.append((candidate2, str1[2:]))
    return candidates
        

def get_num_alpha_code(str1):
    if str1 == '':
        print 'end of string'
        return 0
    else:
        count = 0
        for code, substr in get_valid_codes(str1):
            print code, substr
            count += 1
            num_substr = get_num_alpha_code(substr)
            count += num_substr
        return count
    

def process():
    while True:
        str1 = raw_input()
        if str1 == '0':
            break
        else:
            length = len(str1)
            print get_num_alpha_code(str1)


x = '25114'
# print get_valid_codes(x)
x = '12'
node = Node('#')
print get_num_alpha_code(x)
