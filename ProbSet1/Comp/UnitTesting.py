# since the earlier function was not returning the smallest error for perfect squares , 1 had
# to be added in order that the test runs as it first failed at argument 4 as it was returning 4
#as the smallest prime integer.
def smallest_factor(n):
    if n==1: return 1
    for i in range(2, int(n**.5)+1):
        if n % i == 0: return i
    return n

#problem 2
def month_length(month, leap_year=False):
    """return the number of days in the given month"""
    if month in {"september","april","june","november"}:
        return 30
    elif month in {"january","march","May","july",
                   "august","october","december"}:
        return 31
    if month=="february":
        if not leap_year:
            return 28
        else:
            return 29
    else:
        return None
# problem3:
def operate(a, b, oper):
    """Apply an arithmetic operation to a and b."""
    if type(oper) is not str:
        raise TypeError("oper must be a string")
    elif oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b == 0:
            raise ZeroDivisionError("division by zero is undefined")
        return a / b
    raise ValueError("oper must be one of '+', '/', '-', or '*'")

# problem 4:
