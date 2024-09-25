"""
The driver code for the Roman Numeral calculator.

Run -h or --help as a cmd line argument for more details.
"""
import argparse

from .utils import romanToDecimal, decimalToRoman
from .evaluate_expression import evaluate

def main() -> (str | int):
    """
    Driver code (main function) for the calculator.
    
    Returns:
    - str: If successful run with parsing a Roman Numeral equation to a single Roman_numeral. 
        The alternative is the error in string form from ValueError or IndexError.
    - int: If only put in one argument
    """
    parser = argparse.ArgumentParser(description="Processes a Roman Numeral equation with (+, -, *, / (), [] ). using PEMDAS")
    
    parser.add_argument('equation', nargs=argparse.REMAINDER, help='The equation that is of cmd line arguments, either inputted as a string "" or as a line of Roman Numerals and operations')

    args = parser.parse_args()

    RN_set = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}

    if len(args.equation) == 0:
        print("I don't know how to read this.") # User inputted nothing
        return "I don't know how to read this."
    elif len(args.equation) == 1 and all(c in RN_set for c in args.equation[0]):
        # •	Entry of a number into your application without any operations or other numbers 
        # should simply print the number as their English numeral representation, 
        # i.e. VI should print 6.
        num_res = romanToDecimal(str(args.equation[0]))
        print(num_res)
        return num_res


    roman_equation = " ".join(args.equation) #Add spaces between the equation for edge cases

    # print(f"The roman numeral equation is {roman_equation}")
    operators = {'+', '-', '*', '/', '(', ')', '[', ']'}
    number_equation = ""

    idx = 0

    try:
        prev_num = False

        while idx < len(roman_equation):
            tmp = ""
            if roman_equation[idx] in RN_set:
                if prev_num:
                    raise ValueError("I don't know how to read this.") # handles if there is just a space and no operation
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
                raise ValueError("I don't know how to read this.")

        num_res = evaluate(number_equation)
        roman_res = decimalToRoman(num_res)
        print(roman_res)
        return roman_res
 
    except (ValueError, IndexError) as e:
        print(e)
        return str(e)


if __name__ == "__main__":
    main()
