# Roman_Calculator
A roman numeral that reads in roman numerals from I (1) - MMMCMXCIX (3,999) and operations (+, -, *, /) into a command line using argparse.


# How to run using a script
1) Execute the script in cmd line
```python main.py X```


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
Windows:
```
./venv/Scripts/calculator V + I
```

**NOTE:** Some characters you have to escape in linux like * and ()

