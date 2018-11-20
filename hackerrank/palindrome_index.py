
def is_palindrome(s, begin, end):
    if begin < end:
        if s[begin] != s[end]:
            return False
        else:
            return is_palindrome(s, begin+1, end-1)
    else:
        return True

def is_pal(s):
    return is_palindrome(s, 0, len(s)-1)

def palindrome_index(s):
    no_solution = False
    count = 0
    begin = 0
    end = len(s) - 1
    skip = -1
    while begin < end:
        if s[begin] != s[end]:
            s_begin_removed = s[0:begin] + s[begin+1:len(s)]
            if is_pal(s_begin_removed):
                return begin
            else:
                s_end_removed = s[0:end] + s[end+1:len(s)]
                if is_pal(s_end_removed):
                    return end
                return skip
        begin += 1
        end -= 1
    return skip


def main():
    print(123)
    t = int(input())
    for _ in range(t):
        s = input()
        print(palindrome_index(s))

main()

