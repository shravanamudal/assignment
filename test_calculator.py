import pytest
from calculator import Calculator

def test_add():
  calculator = Calculator()
  assert calculator.add(1, 2) == 3

def test_subtract():
  calculator = Calculator()
  assert calculator.subtract(3, 2) == 1

def test_multiply():
  calculator = Calculator()
  assert calculator.multiply(2, 3) == 6

def test_divide():
  calculator = Calculator()
  assert calculator.divide(6, 2) == 3

if __name__ == "__main__":
  pytest.main()
