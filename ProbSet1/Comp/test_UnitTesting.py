import UnitTesting as ut
import pytest as pt
def test_smallest_factor():
    assert ut.smallest_factor(1)==1, "Fails for 1"
    assert ut.smallest_factor(2)==2, "Fails for 2"
    assert ut.smallest_factor(3)==3, "Fails for 3"
    assert ut.smallest_factor(4)==2, "Fails for 4"
    assert ut.smallest_factor(5)==5, "Fails for 5"
    assert ut.smallest_factor(6)==2, "Fails for 6"
    assert ut.smallest_factor(10)==2, "Fails for 10"

def test_month_length():
    assert ut.month_length("september")==30, "Fails for 30 days "
    assert ut.month_length("january")==31, "fails for 31 days"
    assert ut.month_length("february")==28, "fails for 28 days"
    assert ut.month_length("february", leap_year=True)==29, "fails for 29 days"
    assert ut.month_length("not a month")==None, "fails for not being a month"

def test_operate():
    assert ut.operate(3, 6, '+')==9, "Addition"
    assert ut.operate(3, 6, '-')==-3, "Subtraction"
    assert ut.operate(3, 6, '*')==18, "Multiplication"
    assert ut.operate(3, 6, '/')==.5, "Division"
    with pt.raises(ZeroDivisionError) as excinfo:
        ut.operate(3, 0, "/")
    assert excinfo.value.args[0] == "division by zero is undefined"
    with pt.raises(TypeError) as excinfo:
        ut.operate(3, 6, 7)
    assert excinfo.value.args[0] == "oper must be a string"
    with pt.raises(ValueError) as excinfo:
        ut.operate(3, 6, "Not operator")
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"
