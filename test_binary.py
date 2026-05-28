import pytest
from utils import to_binary


def test_valid_conversion():
    assert to_binary(5) == "101"
    assert to_binary(10) == "1010"
    assert to_binary(0) == "0"
    assert to_binary(100) == "1100100"


def test_out_of_range():
    with pytest.raises(ValueError):
        to_binary(-1)

    with pytest.raises(ValueError):
        to_binary(101)


def test_not_integer():
    with pytest.raises(ValueError):
        to_binary(3.14)
