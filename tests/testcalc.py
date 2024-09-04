import pytest
from Roman_numeral_calc.utils import romanToDecimal, decimalToRoman
from Roman_numeral_calc.evaluate_expression import evaluate


def test_I():
    assert romanToDecimal("I") == 1


def test_V():
    assert romanToDecimal("V") == 5


def test_1():
    assert decimalToRoman(10) == 'X'



def test_eval_expr1():
    assert evaluate("((10 + 5) * 3 - 5 )/ 5") == 8

def test_bad_inputzero():
    with pytest.raises(ValueError) as excinfo:  
        decimalToRoman(0)  
        assert str(excinfo.value) == "Number cannot be 0 or below"

