import pytest

from Roman_numeral_calc.evaluate_expression import evaluate, apply_operator
from collections import deque

# Evaluate function tests with mathematical expressions
def test_eval_1():
    assert evaluate("((10 + 5) * 3 - 5 )/ 5") == 8

def test_bad_inputZero():
    with pytest.raises(ValueError) as excinfo:
        evaluate("1-1")
    assert str(excinfo.value) == "0 does not exist in Roman numerals."

def test_negative():
    with pytest.raises(ValueError) as excinfo:
        evaluate("4-5")
    assert str(excinfo.value) == "Negative numbers can’t be represented in Roman numerals."

def test_eval_float():
    with pytest.raises(ValueError) as excinfo:
        evaluate("4/5")
    assert str(excinfo.value) == "There is no concept of a fractional number in Roman numerals."

def test_eval_nothing():
    with pytest.raises(ValueError) as excinfo:
        evaluate("")
    assert str(excinfo.value) == "I don’t know how to read this."

def test_eval_none():
    with pytest.raises(ValueError) as excinfo:
        evaluate(None)
    assert str(excinfo.value) == "I don’t know how to read this."

def test_eval_parenthesis_brackets():
    assert evaluate("[(10 + 2) * 3] / 12") == 3

def test_invalid_operator():
    with pytest.raises(ValueError) as excinfo:
        evaluate("10 & 5")
    assert str(excinfo.value) == "I don’t know how to read this."

def test_missing_operand():
    with pytest.raises(IndexError) as excinfo:
        evaluate("10 +")
    assert str(excinfo.value) == "I don’t know how to read this."

def test_missing_operator():
    with pytest.raises(IndexError) as excinfo:
        evaluate("10 10")
    assert str(excinfo.value) == "I don’t know how to read this."

def test_only_operators():
    with pytest.raises(IndexError) as excinfo:
        evaluate("++")
    assert str(excinfo.value) == "I don’t know how to read this."

def test_unbalanced_parenthesis():
    with pytest.raises(IndexError) as excinfo:
        evaluate("(10 + 5")
    assert str(excinfo.value) == "I don’t know how to read this."

def test_unbalanced_brackets():
    with pytest.raises(IndexError) as excinfo:
        evaluate("[10 + 5")
    assert str(excinfo.value) == "I don’t know how to read this."

def test_whitespace_only():
    with pytest.raises(ValueError) as excinfo:
        evaluate("   ")
    assert str(excinfo.value) == "I don’t know how to read this."

def test_large_result():
    with pytest.raises(ValueError) as excinfo:
        evaluate("2000 + 2000")
    assert str(excinfo.value) == "You’re going to need a bigger calculator."

def test_complex_expression():
    assert evaluate("((100 + 50) * 2 - 10) / 10") == 29

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError) as excinfo:
        evaluate("10 / 0")
    assert str(excinfo.value) == "You can't divide by 0."

def test_invalid_character():
    with pytest.raises(ValueError) as excinfo:
        evaluate("10 + a")
    assert str(excinfo.value) == "I don’t know how to read this."

def test_unmatched_closing_parenthesis():
    with pytest.raises(IndexError) as excinfo:
        evaluate("10 + 5)")
    assert str(excinfo.value) == "I don’t know how to read this."

def test_invalid_op():
    with pytest.raises(ValueError) as excinfo:
        apply_operator(deque(['^']), deque([9, 5]))
    assert str(excinfo.value) == "I don’t know how to read this."
