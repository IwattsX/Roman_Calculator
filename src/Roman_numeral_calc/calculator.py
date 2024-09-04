"""
The driver code for the Roman Numeral calculator.

Run -h or --help as a cmd line argument for more details.
"""
import argparse

from .utils import romanToDecimal, decimalToRoman
from .evaluate_expression import evaluate

def main():
    """
    Driver code (main function) for the calculator.
    
    Returns:
    - str: If successful run with parsing a Roman Numeral equation to a single Roman_numeral.
    - None: If unsuccessful.
    """
    parser = argparse.ArgumentParser(description="Processes a Roman Numeral equation with (+, -, *, / ). using PEMDAS")
    
    parser.add_argument('equation', nargs=argparse.REMAINDER, help='The equation that needs to be inputed either as a string or a set of cmd line arguments')

    args = parser.parse_args()

    if len(args.equation) == 0:
        print("I don’t know how to read this.") # User inputted nothing
        return None
    elif len(args.equation) == 1: # Handles if the user only inputted one thing
        try:
            num_res = romanToDecimal(str(args.equation[0]))
            print(num_res)
        except ValueError as e:
            print(e)
        return


    roman_equation = " ".join(args.equation) #Add spaces between the equation for edge cases

    # print(f"The roman numeral equation is {roman_equation}")

    RN_set = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    operators = {'+', '-', '*', '/', '(', ')', '[', ']'}
    number_equation = ""

    idx = 0

    try:
        prev_num = False

        while idx < len(roman_equation):
            tmp = ""
            if roman_equation[idx] in RN_set:
                if prev_num:
                    raise ValueError("I don’t know how to read this.") # handles if there is just a space and no operation
                while idx < len(roman_equation) and roman_equation[idx] in RN_set:
                    tmp += roman_equation[idx]
                    idx += 1
                number_equation += str(romanToDecimal(tmp))
                prev_num = True
            
            elif roman_equation[idx] in operators:
                number_equation += roman_equation[idx]
                idx += 1
                prev_num = False
            
            elif roman_equation[idx].isspace():
                idx += 1

            else:
                raise ValueError("I don’t know how to read this.")

        num_res = evaluate(number_equation)
        roman_res = decimalToRoman(num_res)
        print(roman_res)
 
    except (ValueError, IndexError) as e:
        print(e)
        return None


if __name__ == "__main__":
    main()