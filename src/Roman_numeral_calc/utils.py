import re


def romanToDecimal(roman_number : str) -> int:
    if not isinstance(roman_number, str):
        raise ValueError("The roman number must be in string format...")

    regexp_valid = r'^(^IVXLCDM)'

    if re.search(regexp_valid, roman_number) is not None:
        raise ValueError("The roman number must have only I, V, X, L, C, D, M")


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
            

    return res

def decimalToRoman(num : int) -> str:
    if not isinstance(num, int):
        raise ValueError("I don’t know how to read this.")

    if num == 0:
        raise ValueError("0 does not exist in Roman numerals.")
    elif num < 0:
        raise ValueError("Negative numbers can’t be represented in Roman numerals.")
    
    if num > 3999:
        raise ValueError("ou’re going to need a bigger calculator.")
    
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
        

if __name__ == '__main__':
    for i in range(1, 101):
        roman_number = decimalToRoman(i)
        print(roman_number)
        print(romanToDecimal(roman_number))
        print("------")

    try: 
        print(decimalToRoman(0))
    except ValueError as e:
        print(e)
