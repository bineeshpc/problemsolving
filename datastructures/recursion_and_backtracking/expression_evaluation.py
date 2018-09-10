# ! /usr/bin/env python
import six

def evaluate(expr):
    """
    evaluate("7") -> 7
    evaluate("(2+3)") -> 5
    evaluate("((2+3)*(1+2))") -> 15
    """
    def isdigit(ch):
        try:
            int(ch)
            return True
        except ValueError:
            return False

    def evaluate_helper(expr, index):
        ch = expr[index]
        if ch == '(':
            # complex
            index += 1  # move past (

            # get the left operand
            left, index = evaluate_helper(expr, index)
            opr = expr[index]
            index += 1  # move past the operator

            # get the right operand
            right, index = evaluate_helper(expr, index)
            index += 1  # to move past closing paranthesis
            if opr == '+':
                return left + right, index
            elif opr == '*':
                return left * right, index

  
        else:
            if isdigit(ch):
                value = 0
                while isdigit(ch):
                    value = value * 10 + int(ch)
                    index += 1
                    if index < len(expr):
                        ch = expr[index]
                    else:
                        break
                return value, index

            

    return evaluate_helper(expr, 0)[0]



def evaluate1(expr):
    """
    This code assumes that we have all 
    operands are surrounded by paranthesis
    evaluate("(2+3)") -> 5
    evaluate("((2+3)*(1+2))") -> 15
    """
    operators = '*/+-'
    operator_stack = []
    operand_stack = []

    def parse_operand(s, i):
        """
        parse the location of the string until I find an
        operator
        parse "12" to 12
        "12.12" to 12.12
        returns a float
        """
        value = ''
        while (s[i] not in operators):
            value += s[i]
            i += 1
            if s[i] == ')':
                break
        return float(value), i-1

    def do_operation(operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2 
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        elif operator == '-':
            return operand1 - operand2

    i = 0
    s = expr
    length = len(s)
    numbers = '0123456789'
    while i < length:
        data = s[i]
        if data == '(':
            operand_stack.append(data)
        elif data in numbers:
            # parse the operand number and modifies the index i
            number, i = parse_operand(s, i)
            operand_stack.append(number)
        elif data in operators:
            operator_stack.append(data)
        elif data is ')':
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            operator = operator_stack.pop()
            operand_stack.pop() # remove (
            operand_stack.append(do_operation(operand1, operand2, operator))
        i += 1
    return operand_stack.pop()




def main():
    t = int(six.moves.input())
    for _ in range(t):
        expression = six.moves.input()
        six.print_(expression,  evaluate1(expression))


if __name__ == '__main__':
    main()