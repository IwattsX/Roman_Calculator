import re
from collections import deque

def peek(stack):
    """
    Peeks at the top element of a stack without popping it.
    """
    return stack[-1] if stack else None

def apply_operator(operators, values):
    """
    Applies an operator to the two most recent values in the values stack.
    """
    if not operators or len(values) < 2:
        raise IndexError("INVALID EQUATION: Either no operator or the left/right values aren't there")
        
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    
    res = 0
    if operator == '+':
        res = left + right
    elif operator == '-':
        res = left - right
    elif operator == '*':
        res = left * right
    elif operator == '/':
        if left % right == 0:
            res = left // right
        else:
            raise ValueError("No float numbers allowed during roman times")
            print("ERROR for {left} / {right}")
    else:
        raise ValueError("Not an allowed operator")


    values.append(res)

def greater_precedence(op1, op2):
    """
    Determines if the precedence of op1 is greater than op2.
    """
    precedences = {'+' : 0, '-' : 0, '*' : 1, '/' : 1}
    return precedences[op1] > precedences[op2]

def evaluate(expression):
    """
    Evaluates a mathematical expression using the Shunting Yard Algorithm.
    """
    tokens = re.findall("[+/*()-]|\d+", expression)
    print(tokens)
    values, operators = deque([]), deque([])
    try:
        for token in tokens:
            if token.isdigit():
                values.append(int(token))
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while peek(operators) and peek(operators) != '(':
                    apply_operator(operators, values)
                operators.pop() # Discard the '('
            else:
                while peek(operators) and peek(operators) not in "()" and greater_precedence(peek(operators), token):
                    apply_operator(operators, values)
                operators.append(token)
        while peek(operators):
            apply_operator(operators, values)
    except ValueError as e:
        return e

    return values[0]

# Example demonstration:
def main():
    expression = '((20 - 10 ) * (30 - 20) / 33 + 10 ) * 2'
    print("Shunting Yard Algorithm Result:", evaluate(expression))
    print("Native Python Evaluation:", eval(expression))

if __name__ == '__main__':
    main()
