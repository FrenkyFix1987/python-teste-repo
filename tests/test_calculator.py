import math
from src.calculator import add, sub, mul, div
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(10, 3) == 7
    assert sub(0, 5) == -5

def test_mul():
    assert mul(4, 2.5) == 10
    assert mul(-3, 3) == -9

def test_div():
    assert div(10, 4) == 2.5
    assert math.isclose(div(1, 3), 0.3333333333, rel_tol=1e-9)

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(1, 0)
