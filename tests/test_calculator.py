import pytest
from calculator.calculator import Calculator

class TestCalculator:
    @pytest.fixture
    def calculator(self):
        return Calculator()

    def test_add(self, calculator):
        assert calculator.add(1, 2) == 3
        # additional test cases...

    def test_subtract(self, calculator):
        assert calculator.subtract(10, 5) == 5
        # additional test cases...

    def test_multiply(self, calculator):
        assert calculator.multiply(2, 3) == 6
        # additional test cases...

    def test_divide(self, calculator):
        assert calculator.divide(10, 5) == 2
        # additional test cases...
        with pytest.raises(ZeroDivisionError):
            calculator.divide(10, 0)
