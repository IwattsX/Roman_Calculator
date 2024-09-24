# Roman_Calculator
A roman numeral that reads in roman numerals from I (1) - MMMCMXCIX (3,999) and operations (+, -, *, /) into a command line using argparse.


# How to run using a script
1) Execute the script in cmd line
```python main.py X```

**NOTE** Make sure to ```pip install .``` first before you do this just like the virtual environment

# How to Run via using the pyproject.toml file
1) Create a virtual Env:
```
python -m venv venv
```

2) activate the virtual environment
- Linux:
```
source venv/bin/activate
```
- Windows:
```
./venv/Scripts/activate
```

3) Install this using pyproject.toml file via pip
To put in editable mode
```
pip install -e .
```

Install normally
```
pip install .
```

**NOTE:** Default directory for the execulable is inside the $PATH/venv/bin/calculator

4) Run the calculator
- Linux:
```
./venv/bin/calculator V + I
```
- Windows:
```
./venv/Scripts/calculator V + I
```

**NOTE:** Some characters you have to escape in linux like * and ()

# Run test using pytest with pytest-cov
- Integration test using monkeypatch
```
pytest --cov=src.Roman_numeral_calc.calculator --cov-report=term-missing tests/test_calculator.py
```

- For only utils.py functions romanToDecimal() and decimalToRoman()
```
pytest --cov=src.Roman_numeral_calc.utils --cov-report=term-missing tests/test_utils.py
```

- For only evaluate_expression.py test
```
pytest --cov=src.Roman_numeral_calc.evaluate_expression --cov-report=term-missing tests/test_evaluation.py
```

- For both utils.py and evaluate_expression.py
```
pytest --cov=src.Roman_numeral_calc.evaluate_expression --cov=src.Roman_numeral_calc.utils  --cov-report=term-missing tests/run_unit_test.py
```
# Run test w/o pytest-cov
- Integration test using monkeypatch
```
pytest tests/test_calculator.py
```

- For only utils.py functions romanToDecimal() and decimalToRoman()
```
pytest tests/test_utils.py
```
- For only evaluate_expression.py test
```
pytest tests/test_evaluation.py
```

- For both utils.py and evaluate_expression.py
```
pytest tests/run_unit_test.py
```

