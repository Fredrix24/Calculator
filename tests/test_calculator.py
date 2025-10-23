# tests/test_calculator.py
from calculator import add, subtract, multiply, divide  # Импорт из пакета 'calculator'
import pytest # Импортируем pytest (обычно это не нужно, но иногда помогает)

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(5, 2) == 2.5
    assert divide(10, 0) == "Error: Division by zero"