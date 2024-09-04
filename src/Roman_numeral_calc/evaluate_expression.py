import re
from collections import deque

def peek(stack : deque) -> str:
    """
    Peeks at the top element of a stack without popping it.
    """
    return stack[-1] if stack else None

def apply_operator(operators : deque, values : deque):
    """
    Applies an operator to the two most recent values in the values stack.
    """
    if not operators or len(values) < 2:
        print("Hello")
        raise IndexError("I don’t know how to read this.")
        
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    
    res = 0
    # Under natural number closure will still result in natural number, but handle 3,999 <
    if operator == '+':
        res = left + right
        if res > 3999:
            raise ValueError("You’re going to need a bigger calculator.")
    
    # Natural number closure does not hold here if left <= right (only time it can be 0 or negative)
    elif operator == '-':
        res = left - right
        if res == 0:
            raise ValueError("0 does not exist in Roman numerals.")
        elif res < 0:
            raise ValueError("Negative numbers can’t be represented in Roman numerals.")
    
    # Multiplying two natural nums will always result in a natural number
    elif operator == '*':
        res = left * right
    
    # Only if left is divisible by the right will this work
    elif operator == '/':
        if left % right == 0:
            res = left // right
        else:
            raise ValueError("There is no concept of a fractional number in Roman numerals.")
    else:
        raise ValueError("I don’t know how to read this.")


    values.append(res)

def greater_precedence(op1 : str, op2 : str) -> bool:
    """
    Determines if the precedence of op1 is greater than op2.
    """
    precedences = {'+' : 0, '-' : 0, '*' : 1, '/' : 1}
    return precedences[op1] > precedences[op2]

def evaluate(expression : str) -> int:
    """
    Evaluates a mathematical expression using the Shunting Yard Algorithm.
    """
    tokens = re.findall("[+/*()-\[\]]|\d+", expression)
    print(tokens)
    values, operators = deque(), deque()

    for token in tokens:
        if token.isdigit():
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == '[':
            operators.append(token)
        elif token == ')':
            while peek(operators) and peek(operators) != '(':
                apply_operator(operators, values)
            operators.pop() # Discard the '('
        elif token == ']':
            while peek(operators) and peek(operators) != '[':
                apply_operator(operators, values)
            operators.pop() # Discard the '['
        else:
            while peek(operators) and peek(operators) not in "()[]" and greater_precedence(peek(operators), token):
                apply_operator(operators, values)
            operators.append(token)
    
    while peek(operators):
        apply_operator(operators, values)
    

    return values[0]