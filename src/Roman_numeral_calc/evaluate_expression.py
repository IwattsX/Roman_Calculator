"""A File used for evaluation a mathematical expression using the shutting yard algorithm."""

import re
from collections import deque


def peek(stack : deque) -> (str | None) :
    """
    Peeks at the top element of a stack without popping it.

    Parameters:
    - stack: a deque of operation tokens

    Returns:
    - None: if the stack is empty
    - str: the last element of the deque
    """
    return stack[-1] if stack else None

def apply_operator(operators : deque, values : deque):
    """
    Apply an operator to the two most recent values in the values stack. Appends the result to the values deque.

    Parameters: 
    - operators (deque): Stack of operations to do
    - values (deque): contains the left and right value to the operator

    Raises:
    - IndexError: If there is not enough values to pop for either operators or values
    - ValueError: If result is greater than 3,999 or is less than or equal to 0 as well as a floating point number
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
    Determine the presedence between two operations (+, -, *, / ).

    Returns: 
    - bool: true the op1 has greater precedence than op2 else false
    """
    precedences = {'+' : 0, '-' : 0, '*' : 1, '/' : 1}
    return precedences[op1] > precedences[op2]

def evaluate(expression : str) -> int:
    """
    Evaluate a mathematical expression using the Shunting Yard Algorithm.

    Parameters: 
    - expression (str): a mathematical expression with regular numbers and operations (+, -, *, / )
    and supports parenthesis and brackets.
    
    Returns:
    - int: The result of evaluating the mathematical expression. 

    Raises:
    - ValueError: if the expression is invalid
    - IndexError: if either the left, right, or operator is missing since the stack will have an indexError for popping
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