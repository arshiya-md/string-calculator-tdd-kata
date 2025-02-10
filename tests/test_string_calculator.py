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