# Roman_Calculator

# How to Run
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

