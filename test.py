from arithmetics import Arithmetics
app = Arithmetics()

def test_addition():
    add = app.addition(3,7)
    assert 10 == add

def test_subtraction():
    sub = app.subtraction(10,5)
    assert 5 == sub

def test_multiplication():
    multiply = app.multiplication(2, 8)
    assert 16 == multiply

def test_division():
    divide = app.division(10, 5)
    assert 2 == divide