"""The file used to translate roman numerals to integers and vice versa."""

import re


def romanToDecimal(roman_number : str):
    """
    Parse a roman_number (I, V, X, L, C, D, M) into a number.
    
    Parameters:
    - roman_number: A string representing the Roman numeral (I, V, X, L, C, D, M).

    Returns:
    - int: the integer representation of the roman numeral
    
    Raises:
    - ValueError: the Roman numeral is invalid or is not a string type
    """
    # Should never happen
    if not isinstance(roman_number, str):
        raise ValueError("I don't know how to read this.")
    
    if roman_number == "":
        raise ValueError("I don't know how to read this.")
    
    # See this for more details on how this regexp works
    # https://www.geeksforgeeks.org/validating-roman-numerals-using-regular-expression/ 
    regexp_valid = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

    if not re.search(regexp_valid, roman_number):
        raise ValueError("I don't know how to read this.")

    res = 0
    conversions = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    
    n = len(roman_number)
    i = 0
    while i < n:
        tmp1 = conversions[roman_number[i]]

        if i + 1 < n:
            tmp2 = conversions[roman_number[i+1]]
        

            if tmp1 >= tmp2:
                res += tmp1
            else:
                res += (tmp2 - tmp1)
                i += 1
        else:
            res += tmp1
        i += 1
    
    # No longer need this since the regexp handles it
    # if res > 3999:
    #     raise ValueError("You're going to need a bigger calculator.")
    
    return res

def decimalToRoman(num : int):
    """
    Parse a natural number to a Roman Numeral.

    Parameters:
    - num: the integer that needs to be parsed into a Roman Numeral.
    
    Returns:
    - str: The roman numeral.

    Raises:
    - ValueError: If num isn't an integer type or num<=0 or num > 3999
    """
    if not isinstance(num, int):
        raise ValueError("I don't know how to read this.")

    if num == 0:
        raise ValueError("0 does not exist in Roman numerals.")
    elif num < 0:
        raise ValueError("Negative numbers can't be represented in Roman numerals.")
    
    if num > 3999:
        raise ValueError("You're going to need a bigger calculator.")
    
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    s = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    res = ""
    i = 0
    while num > 0:
        if num >= nums[i]:
            res = res + s[i]
            num -= nums[i]
        else:
            i += 1

    return res
