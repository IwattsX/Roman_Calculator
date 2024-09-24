import pytest
from src.Roman_numeral_calc.calculator import main

# Integration testing for calculator.py

def test_single_roman_numeral(monkeypatch, capsys):
    # Simulate the command line argument `./venv/bin/calculator V`
    monkeypatch.setattr('sys.argv', ['calculator', 'V'])

    # Call the main function
    val = main()

    # Capture the output
    captured = capsys.readouterr()

    # Check the output
    assert captured.out.strip() == '5'
    assert val == 5

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
