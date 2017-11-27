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
    Transform the algebraic expression with brackets 
    into RPN form (Reverse Polish Notation). 
    Two-argument operators: +, -, *, /, ^ 
    (priority from the lowest to the highest),
    brackets ( ). 
    Operands: only letters: a,b,...,z. 
    Assume that there is only one RPN form 
    (no expressions like a*b*c). 

    we need an operator stack
    we need an operand stack
    consider operator precedance
    parathesis will have hightest precedance
    paranthesis can probably be pushed into operand stack

    +, -, *, /, ^  (operator precedance from low to high)
    Consider case 1: a+b*c
    
    we get a
    it is an operand
    output it
    
    we get +
    it is an operator
    since stack is empty
    push to operator stack
    
    we get b
    it is an operand
    output it

    we get * 
    it is an operator
    peek into stack
    stack contains + on top.
    push * to the stack
    
    now the expression is complete.
    we see end of it.
    pos all elements from operator stack and output it
        
    Consider case2: (a+b)*c

    ( since it is bracket push to operator stack

    a operand output it
    + operator push to stack
    b operand output it
    ) pop everything until i find ) and output it
    * since stack is empty push it
    c operand output it
    
    pop everything from stack and output it
    """
    postfix = []
    print expression
    length_of_expression = len(expression)
    stack = Stack(length_of_expression)
    for letter in expression:
        print letter
        print "postfix", postfix
        print stack
        if is_operand(letter):
            postfix.append(letter)
        else:
            if stack.is_empty():
                stack.push(letter)
                continue
            top = stack.peek()
            if get_precedance(letter) > get_precedance(top):
                stack.push(letter)
            else:
                # pop everything from stack until the precedance of operator
                # from stack is less than or equal to precedance of current operators
                print "letter", letter
                while get_precedance(stack.peek()) > get_precedance(letter):
                    top = stack.pop()
                    postfix.append(top)
        if letter == '(':
            stack.push(letter)
        elif letter == ')':
            while stack.peek() != '(':
                top = stack.pop()
                postfix.append(top)
            stack.pop()  # pop out the '(' character

    while not stack.is_empty():
        postfix.append(stack.pop())
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
    if operator == '(' or operator == ')':
        return 100
    else:
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
        stack_size = len(infix)
        assert infix_to_postfix(infix) == postfix
        print infix, postfix


def process():
    num_testcases = int(raw_input())
    count = 0
    while count < num_testcases:
        value = raw_input()
        print infix_to_postfix(value)
        count += 1


# process()
test()
