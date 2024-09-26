"""A File used for evaluation a mathematical expression using the shutting yard algorithm."""

import re
from collections import deque


def peek(stack : deque):
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
        raise IndexError("I don't know how to read this.")
        
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    
    res = 0
    # Under natural number closure will still result in natural number, but handle 3,999 <
    if operator == '+':
        res = left + right
        if res > 3999:
            raise ValueError("You're going to need a bigger calculator.")
    
    # Natural number closure does not hold here if left <= right (only time it can be 0 or negative)
    elif operator == '-':
        res = left - right
        if res == 0:
            raise ValueError("0 does not exist in Roman numerals.")
        elif res < 0:
            raise ValueError("Negative numbers can't be represented in Roman numerals.")
    
    # Multiplying two natural nums will always result in a natural number
    elif operator == '*':
        res = left * right
        if res > 3999:
            raise ValueError("You're going to need a bigger calculator.")

    
    # Only if left is divisible by the right will this work
    elif operator == '/':
        # Never should get here
        if right == 0:
            raise ZeroDivisionError("You can't divide by 0.")
        elif left % right == 0:
            res = left // right
        else:
            raise ValueError("There is no concept of a fractional number in Roman numerals.")
    else:
        raise ValueError("I don't know how to read this.")


    values.append(res)

def greater_precedence(op1 : str, op2 : str):
    """
    Determine the presedence between two operations (+, -, *, / ).

    Returns: 
    - bool: true the op1 has greater precedence than op2 else false
    """
    precedences = {'+' : 0, '-' : 0, '*' : 1, '/' : 1}
    return precedences[op1] > precedences[op2]

def evaluate(expression : str):
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
    if not isinstance(expression, str) or expression.strip() == "":
        raise ValueError("I don't know how to read this.")
    
    # Ensure expression is valid by checking for invalid characters
    valid_tokens = re.findall(r'\d+|[+*/()-\[\]]', expression)
    if "".join(valid_tokens) != expression.replace(" ", ""):
        raise ValueError("I don't know how to read this.")

    tokens = valid_tokens
    values, operators = deque(), deque()

    for token in tokens:
        if token.isdigit():
            values.append(int(token))
        
        elif token in "([":  # Opening brackets/parentheses
            operators.append(token)
        
        elif token in ")]":  # Closing brackets/parentheses
            while peek(operators) and peek(operators) not in "([":  # Apply until matching opening bracket/parenthesis
                apply_operator(operators, values)
            if not operators:
                raise IndexError("I don't know how to read this.")
            operators.pop()  # Discard the matching opening bracket/parenthesis
        
        else:  # Operators +, -, *, /
            while (peek(operators) and
                   peek(operators) not in "()[]" and
                   greater_precedence(peek(operators), token)):
                apply_operator(operators, values)
            operators.append(token)
    
    while operators:
        if peek(operators) in "()[]":
            raise IndexError("I don't know how to read this.")
        apply_operator(operators, values)
    
    if len(values) != 1:
        raise IndexError("I don't know how to read this.")
    
    return values[0]