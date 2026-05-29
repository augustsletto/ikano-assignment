import pytest

from app.calculations.fibonacci import fibonacci

def test_zero():
    assert fibonacci(0) == 0
    
    
def test_one():
    assert fibonacci(1) == 1
    
def test_basic():
    assert fibonacci(10) == 55
    
def test_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_bool_input():
    with pytest.raises(TypeError):
        fibonacci(True)

def test_string_input():
    with pytest.raises(TypeError):
        fibonacci("Kalimera")
  