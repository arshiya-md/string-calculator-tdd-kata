import pytest
from src.string_calculator import StringCalculator

@pytest.fixture
def calculator():
    return StringCalculator()

def test_empty_string_returns_zero(calculator):
    assert calculator.add("") == 0
    
def test_single_number_returns_itself(calculator):
    assert calculator.add("3") == 3
    
def test_multiple_numbers_returns_sum(calculator):
    assert calculator.add("3, 1, 8, 5") == 17
    
def test_newlines_between_numbers(calculator):
    assert calculator.add("15\n3,1") == 19

def test_different_delimiters(calculator):
    assert calculator.add("//*\n5*8") == 13
    
def test_negative_number(calculator):
    with pytest.raises(ValueError, match="Negative numbers not allowed -5"):
        calculator.add("//#\n-5#10")

def test_multiple_negative_numbers(calculator):
    with pytest.raises(ValueError, match="Negative numbers not allowed -5, -10"):
        calculator.add("//#\n-5#-10")

def test_ignore_numbers_greater_than_1000(calculator):
    assert calculator.add("1001, 1") == 1
        