"""

https://practice.geeksforgeeks.org/problems/decode-the-string/0
This is not a recursive algorithm for the time being
I am going to solve it using 2 stacks and investigate whether I can
solve it recursively

"""

import six

input = six.moves.input

def is_num(c):
    x = False
    try:
        int(c)
        x = True
    except ValueError:
        pass
    return x

"""
23[rf12[ca]]
"""

def decode_string(s):
    integer_stack = []
    character_stack = []
    i = 0
    length = len(s)
    while i < length:
        current_char = s[i]
        if is_num(current_char):
            num = int(current_char)
            # handle multi digit numbers in the following while loop
            while True:
                i += 1
                next_char = s[i]
                if is_num(next_char):
                    num = num * 10 + int(next_char)
                else:
                    break
            integer_stack.append(num)
        current_char = s[i]  # because i might have changed in an attempt to catch mutidigit numbers
        if current_char == '[':
            # push it to character stack
            # get the complete number and add it to integer_stack
            character_stack.append(current_char)
        elif current_char == ']':
            # pop everything from character stack until we see ] and join them together and push it to character stack again
            # print character_stack
            simple_string_lst = []
            # print character_stack
            while character_stack[len(character_stack) - 1] != '[':
                simple_string_lst.append(character_stack.pop())
            # pop out [
            character_stack.pop()
            simple_string = "".join(reversed(simple_string_lst))
            # pop out count from integer stack and add it
            count = integer_stack.pop()
            character_stack.append(simple_string * count)
        elif current_char >= 'a' and current_char <= 'z': # current_char is alphabet
            # push it to character_stack
            character_stack.append(current_char)
            # print current_char, character_stack
        i += 1
    return character_stack.pop()


def process():
    t = int(input())
    for _ in range(t):
        str1 = input()
        six.print_(decode_string(str1))

process()

#print decode_string('22[12[bd]ca]')

