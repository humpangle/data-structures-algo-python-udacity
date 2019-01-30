import pytest
import sys

from fibo_recursion import get_fib1, get_fib


def test_get_fib1():
    assert get_fib1(-1) == -1
    assert get_fib1(0) == 0
    assert get_fib1(1) == 1
    assert get_fib1(2) == 1
    assert get_fib1(3) == 2
    assert get_fib1(4) == 3
    assert get_fib1(5) == 5
    assert get_fib1(6) == 8
    assert get_fib1(9) == 34
    assert get_fib1(11) == 89


def test_get_fib():
    assert get_fib(-1) == -1
    assert get_fib(0) == 0
    assert get_fib(1) == 1
    assert get_fib(2) == 1
    assert get_fib(3) == 2
    assert get_fib(4) == 3
    assert get_fib(5) == 5
    assert get_fib(6) == 8
    assert get_fib(9) == 34
    assert get_fib(11) == 89


if __name__ == "__main__":
    pytest.main(sys.argv)
