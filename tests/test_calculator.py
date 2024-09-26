import pytest
from src.Roman_numeral_calc.calculator import main
from src.Roman_numeral_calc.utils import decimalToRoman, romanToDecimal

# Integration testing for calculator.py

def test_single_invalid_RN(monkeypatch, capsys):
    # Simulate the command line argument `./venv/bin/calculator V`
    monkeypatch.setattr('sys.argv', ['calculator', 'Q'])

    # Call the main function
    val = main()

    # Capture the output
    captured = capsys.readouterr()

    # Check the output
    assert captured.out.strip() == 'I don\'t know how to read this.'
    assert val == 'I don\'t know how to read this.'

def test_valid_expression(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', 'X', '+', 'V'])

    val = main()
    captured = capsys.readouterr()

    assert captured.out.strip() == 'XV'
    assert val == "XV"

def test_invalid_input(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', 'V', 'III'])


    val = main()
    captured = capsys.readouterr()

    assert captured.out.strip() == "I don\'t know how to read this."
    assert val == "I don\'t know how to read this."

def test_complex_expression(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', 'X', '+', 'X', '*', 'II'])

    val = main()
    captured = capsys.readouterr()

    assert captured.out.strip() == 'XXX'
    assert val == "XXX"

def test_no_args(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator'])

    val = main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "I don\'t know how to read this."
    assert val == "I don\'t know how to read this."

def test_invalid_operation(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', "2", "+", "2"])

    val = main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "I don\'t know how to read this."
    assert val == "I don\'t know how to read this."


def test_invalid_IC(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', "IC"])

    val = main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "I don\'t know how to read this."
    assert val == "I don\'t know how to read this."

def test_one_through_3999(monkeypatch, capsys):
    for i in range(1, 4000):
        roman_number = decimalToRoman(i)
        monkeypatch.setattr('sys.argv', ['calculator', roman_number])

        valExpected = romanToDecimal(roman_number)

        val = main()

        captured = capsys.readouterr()
        assert captured.out.strip() == f"{valExpected}"
        assert val == valExpected


def test_need_bigger_calc(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', "MM", "*", "II"])

    val = main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "You're going to need a bigger calculator."
    assert val == "You're going to need a bigger calculator."

def test_for_zero(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', "I" , "-", "I"])

    val = main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "0 does not exist in Roman numerals."
    assert val == "0 does not exist in Roman numerals."

def test_for_float(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', "I" , "/", "II"])

    val = main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "There is no concept of a fractional number in Roman numerals."
    assert val == "There is no concept of a fractional number in Roman numerals."

def test_for_neg(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', "IX" , "-", "XI"])

    val = main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Negative numbers can't be represented in Roman numerals."
    assert val == "Negative numbers can't be represented in Roman numerals."

def test_IVI(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', "IVI"])

    val = main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "I don\'t know how to read this."
    assert val == "I don\'t know how to read this."
