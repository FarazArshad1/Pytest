from app import addition
import pytest

@pytest.mark.xfail()
def test_addition():
    assert addition(3,2) == 5

def test_addition_with_negative_values():
    assert addition(-3,-2) == -5