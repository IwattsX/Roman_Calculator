import pytest

from Roman_numeral_calc.utils import romanToDecimal, decimalToRoman
from Roman_numeral_calc.evaluate_expression import evaluate

# Roman to decimal tests
def test_I():
    assert romanToDecimal("I") == 1

def test_V():
    assert romanToDecimal("V") == 5

def test_XIV():
    assert romanToDecimal("XIV") == 14

def test_IX():
    assert romanToDecimal("IX") == 9

def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:  
        romanToDecimal(5)
    assert str(excinfo.value) == "I don’t know how to read this."

def test_invalid_input_string():
    with pytest.raises(ValueError) as excinfo:  
        romanToDecimal("Q")
    assert str(excinfo.value) == "I don’t know how to read this."

def test_empty_roman():
    with pytest.raises(ValueError) as excinfo:
        romanToDecimal("")
    assert str(excinfo.value) == "I don’t know how to read this."

def test_none_input():
    with pytest.raises(ValueError) as excinfo:
        romanToDecimal(None)
    assert str(excinfo.value) == "I don’t know how to read this."

def test_mixed_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        romanToDecimal("MXA")
    assert str(excinfo.value) == "I don’t know how to read this."


# Decimal to Roman tests
def test_10():
    assert decimalToRoman(10) == 'X'

def test_3888():
    assert decimalToRoman(3888) == 'MMMDCCCLXXXVIII'

def test_max_boundary():
    assert decimalToRoman(3999) == "MMMCMXCIX"

def test_bad_inputzero():
    with pytest.raises(ValueError) as excinfo:  
        decimalToRoman(0)  
    assert str(excinfo.value) == "0 does not exist in Roman numerals."

def test_float():
    with pytest.raises(ValueError) as excinfo:
        decimalToRoman(4.4)
    assert str(excinfo.value) == "I don’t know how to read this."

def test_negative_number():
    with pytest.raises(ValueError) as excinfo:
        decimalToRoman(-1)
    assert str(excinfo.value) == "Negative numbers can’t be represented in Roman numerals."

def test_above_3999():
    with pytest.raises(ValueError) as excinfo:
        decimalToRoman(4000)
    assert str(excinfo.value) == "You’re going to need a bigger calculator."

def test_non_integer_input():
    with pytest.raises(ValueError) as excinfo:
        decimalToRoman("1000")
    assert str(excinfo.value) == "I don’t know how to read this."
