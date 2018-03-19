# http://www.spoj.com/problems/ACODE/

import string

alpha_number = {v: k+1 for k, v in enumerate(string.uppercase)}
number_alpha = [v for v in string.uppercase]


def get_number(alpha):
    return alpha_number[alpha]

def get_alpha(number):
    try:
        alphabet = number_alpha[number - 1]
    except IndexError:
        alphabet = None
    return alphabet
    
def get_alpha_codes(str1):
    single_letter_option = []
    double_letter_option = []
    if len(str1) == 0:
        return ['']
    if len(str1) >= 1:
        single_letter = str1[0]
        single_letter_rest = str1[1:]
        alphabet = get_alpha(int(single_letter))
        if alphabet:
            single_letter_option.extend([(alphabet + i) for i in get_alpha_codes(single_letter_rest)])
    if len(str1) >= 2:
        double_letter = str1[0:2]
        double_letter_rest = str1[2:]
        alphabet = get_alpha(int(double_letter))
        if alphabet:
            double_letter_option.extend([(alphabet + i) for i in get_alpha_codes(double_letter_rest)])

    return single_letter_option + double_letter_option


def get_num_alpha_codes(str1):
    return len(get_alpha_codes(str1))

    
def get_alpha_codes_dp_good(str1, start, end, cache):
    if cache.get((start, end)):
        return cache[(start, end)]
    if start > end:
        return ['']
    single_letter_option = []
    double_letter_option = []
    if end - start >= 0:
        single_letter = str1[start]
        alphabet = get_alpha(int(single_letter))
        if alphabet:
            single_start = start + 1
            single_letter_option = [(alphabet + i) for i in get_alpha_codes_dp_good(str1, single_start, end, cache)]
    if end - start >= 1:
        double_letter = str1[start:start+2]
        alphabet = get_alpha(int(double_letter))
        if alphabet:
            double_start = start + 2
            double_letter_option = [(alphabet + i) for i in get_alpha_codes_dp_good(str1, double_start, end, cache)]
        
    cache[(start, end)] = single_letter_option + double_letter_option
    return cache[(start, end)]


def get_num_alpha_codes_dp_good(str1):
    cache = {}
    print get_alpha_codes_dp_good(str1, 0, len(str1) - 1, cache)
    return len(get_alpha_codes_dp_good(str1, 0, len(str1) - 1, cache))
    

def process():
    while True:
        str1 = raw_input()
        if str1 == '0':
            break
        else:
            print get_num_alpha_codes_dp_good(str1)


# process()

x = '112'
print get_num_alpha_codes_dp_good(x)


