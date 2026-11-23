import pytest
from calculatrice import addition, division

def test_addition():
    assert addition(2, 3) == 5

def test_division():
    assert division(10, 2) == 5
    with pytest.raises(ValueError):
        division(10, 0)
