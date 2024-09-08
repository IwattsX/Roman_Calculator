import pytest
from Roman_numeral_calc.calculator import main

# Integration testing for calculator.py

def test_single_roman_numeral(monkeypatch, capsys):
    # Simulate the command line argument `./venv/bin/calculator V`
    monkeypatch.setattr('sys.argv', ['calculator', 'V'])

    # Call the main function
    main()

    # Capture the output
    captured = capsys.readouterr()

    # Check the output
    assert captured.out.strip() == '5'

def test_single_invalid_RN(monkeypatch, capsys):
    # Simulate the command line argument `./venv/bin/calculator V`
    monkeypatch.setattr('sys.argv', ['calculator', 'Q'])

    # Call the main function
    main()

    # Capture the output
    captured = capsys.readouterr()

    # Check the output
    assert captured.out.strip() == 'I don\'t know how to read this.'

def test_valid_expression(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', 'X', '+', 'V'])

    main()
    captured = capsys.readouterr()

    assert captured.out.strip() == 'XV'

def test_invalid_input(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', 'V', 'III'])


    main()
    captured = capsys.readouterr()

    assert captured.out.strip() == "I don\'t know how to read this."

def test_complex_expression(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', 'X', '+', 'X', '*', 'II'])

    main()
    captured = capsys.readouterr()

    assert captured.out.strip() == 'XXX'

def test_no_args(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator'])

    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "I don\'t know how to read this."

def test_invalid_operation(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['calculator', "2", "+", "2"])

    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "I don\'t know how to read this."
