def reverse(s):
    """ given a string s returns the reverse string """

    def swap(s, i, j):
        s[i], s[j] = s[j], s[i]

    def reverse_helper(s, begin, end):
        # base case
        # recursion terminates when begin becomes >= end
        # recursive case
        if begin < end:
            swap(s, begin, end)
            reverse_helper(s, begin + 1, end - 1)

    s_list = list(s)
    reverse_helper(s_list, 0, len(s_list) - 1)
    return ''.join(s_list)
    


s = "current"
print s
s_r = reverse(s)
print s_r
