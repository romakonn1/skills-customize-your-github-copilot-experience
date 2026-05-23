import pytest
from starter_code import add, is_palindrome, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_is_palindrome():
    assert is_palindrome("Race car") is True
    assert is_palindrome("hello") is False


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(1, 0)
