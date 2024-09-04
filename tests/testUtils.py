import pytest
from src.Roman_numeral_calc.utils import romanToDecimal, decimalToRoman

def test_I():
    assert romanToDecimal("I") == 1


def test_V():
    assert romanToDecimal("V") == 5


def test_1():
    assert decimalToRoman(10) == 'X'