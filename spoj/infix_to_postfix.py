# http://www.spoj.com/problems/ONP/

import string
precedance = dict((v, k) for k, v in enumerate(['+', '-', '*', '/', '^']))
operands = {i: True for i in string.lowercase}


class Stack(object):
    def __init__(self, total_size):
        self.total_size = total_size
        self.data = [-1 for _ in range(self.total_size)]
        self.size = 0

    def push(self, element):
        if self.size < self.total_size:
            self.data[self.size] = element
            self.size += 1
        else:
            raise Exception('stack full')

    def pop(self):
        if self.size > 0:
            element = self.data[self.size-1]
            self.size -= 1
            return element
        else:
            raise Exception('stack empty')

    def peek(self):
        if self.size > 0:
            element = self.data[self.size-1]
            return element
        else:
            raise Exception('stack empty')

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def __str__(self):
        
        data = []
        for i in range(self.size):
            data.append(self.data[i])
        return "stack : " + str(data)


def infix_to_postfix(expression):
    """ Given an expression in infix form return 
    it's postfix expression
    
    """
    postfix = []
    stack_size = len(expression)
    stack = Stack(stack_size)
    for c in expression:
        if c == '(':
            stack.push(c)
        elif c == ')':
            while stack.peek() != '(':
                top_element = stack.pop()
                postfix.append(top_element)
            stack.pop()  # pop out the '(' character
        elif is_operand(c):
            postfix.append(c)
        elif is_operator(c):
            while stack.peek() != '(' and get_precedance(stack.peek()) >= get_precedance(c):
                top_element = stack.pop()
                postfix.append(top_element)
            stack.push(c)
    while not stack.is_empty():
        top_element = stack.pop()
        if is_operand(top_element):
            postfix.append(top_element)
    return ''.join(postfix)

def is_operator(letter):
    if precedance.get(letter) is not None:
        return True
    else:
        return False

    
def is_operand(letter):
    if operands.get(letter) is not None:
        return True
    else:
        return False


def get_precedance(operator):
    # bracket will have precedance = 100 for time being
    # if more than 100 operators are added this should change
    return precedance[operator]

def test_precedance():
    print get_precedance('+')
    print get_precedance('^') > get_precedance('/')

def test():
    expressions = ["a+b*c",
                   "(a+b)*c",
                   "(a+(b*c))", 
                   "((a+b)*(z+x))",
                   "((a+t)*((b+(a+c))^(c+d)))"]
    postfixes = ["abc*+",
                 "ab+c*",
                 "abc*+",
                 "ab+zx+*",
                 "at+bac++cd+^*"]
    for infix, postfix in zip(expressions, postfixes):
        infix = "({})".format(infix)
        try:
            output = infix_to_postfix(infix)
            assert output == postfix
        except AssertionError:
            print "Failed"
        finally:
            print infix, postfix, output
            


def process():
    num_testcases = int(raw_input())
    count = 0
    while count < num_testcases:
        value = raw_input()
        print infix_to_postfix(value)
        count += 1


process()
# test()
