import pytest

from app.calculations.factorial import factorial

def test_zero():
    assert factorial(0) == 1
    
def test_large_number():
    assert factorial(52) == 80658175170943878571660636856403766975289505440883277824000000000000
    
def test_basic():
    assert factorial(5) == 120
    
def test_negative():
    with pytest.raises(ValueError):
        factorial(-1)