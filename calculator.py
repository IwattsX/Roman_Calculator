import argparse

from utils import romanToDecimal, decimalToRoman
from evaluate_expression import evaluate

def main():
    parser = argparse.ArgumentParser(description="Process some arguments.")
    
    parser.add_argument('equation', nargs=argparse.REMAINDER, help='A list of arguments')

    args = parser.parse_args()

    # Print the parsed arguments
    roman_equation = "".join(args.equation)
    
    RN_set = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    operators = {'+', '-', '*', '/', '(', ')'}
    number_equation = ""
    idx = 0
    
    print(f"The roman numeral equation is {roman_equation}")
    while idx < len(roman_equation):
        tmp = ""
        if roman_equation[idx] in RN_set:
            while idx < len(roman_equation) and roman_equation[idx] not in operators and roman_equation[idx] != ' ':
                tmp += roman_equation[idx]
                idx += 1
            number_equation += str(romanToDecimal(tmp))
        
        elif roman_equation[idx] in operators:
            number_equation += roman_equation[idx]
            idx += 1
        else:
            idx += 1

    print(f"The base 10 equation being evaluated is {number_equation}")

    try: 
        num_res = evaluate(number_equation)
        roman_res = decimalToRoman(num_res)

        print(roman_res)
 
    except (ValueError, IndexError) as e:
        print(e)



if __name__ == "__main__":
    main()

