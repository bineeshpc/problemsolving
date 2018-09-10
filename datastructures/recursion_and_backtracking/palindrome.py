import six

def ispalindrome(s):
    def ispalindrome_helper(s, begin, end):
        
        if end - begin < 1:
            # this case works better than
            # begin < end
            # because this check works for empty string as well
            return True
        else:
            if s[begin] == s[end]:
                return ispalindrome_helper(s, begin + 1, end - 1)
            else:
                return False
    return ispalindrome_helper(s, 0, len(s) - 1)

def main():
    t = int(six.moves.input())
    for _ in range(t):
        s = six.moves.input()
        six.print_('{}, {}'.format(s, ispalindrome(s)))

if __name__ == '__main__':
    main()