# https://www.hackerrank.com/challenges/sherlock-and-anagrams
# other people solved it in different ways
# one guy has used some prime number hashing(explore later)
# most guys used the count of characters option
# two anagrams will have the same number of character counts

def get_substring_of_length_n(s, n):
    # move a sliding window of length n
    begin = 0
    end = n - 1
    substrings = []
    length = len(s)
    while end < length:
        substrings.append(s[begin:end+1])
        begin += 1
        end += 1
    return substrings

def get_all_substrings(s):
    length = len(s)
    substrings = []
    # 1 upto length - 1
    for i in range(1, length):
        substrings.extend(get_substring_of_length_n(s, i))
    return substrings

def get_all_combinations_nC2(s):
    length = len(s)
    d = {}
    sublist_pairs = []
    for i in range(length):
        for j in range(1, length):
            d[(i, j)] = True
            if (j, i) not in d:
                sublist_pairs.append((s[i], s[j]))
    return sublist_pairs


def get_all_substrings_anagrams(s):
    length = len(s)
    count_of_all_lengths = 0
    # 1 upto length - 1
    for i in range(1, length):
        count = 0
        sorted_substrings = [''.join(sorted(list(substring))) 
        for substring in get_substring_of_length_n(s, i)]
        for a, b in get_all_combinations_nC2(sorted_substrings):
            if a == b:
                count += 1
        #print(count)
        count_of_all_lengths += count
            
    return count_of_all_lengths

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print(get_all_substrings_anagrams(s))

main()