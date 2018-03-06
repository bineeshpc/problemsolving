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

print evaluate("((7+2)*(4+6))")
print evaluate("(70+2)")
print evaluate("5")
print evaluate("542")

print evaluate("((7+2)*4)")
print evaluate("(30*(90+10))")
