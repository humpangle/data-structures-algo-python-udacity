import pytest
import sys

from bubble_sort import bubble_sort


def test1():
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([2, 1]) == [1, 2]
    assert bubble_sort([2, 1, 3]) == [1, 2, 3]

    x = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    assert bubble_sort(x) == sorted(x)


if __name__ == "__main__":
    pytest.main(sys.argv)
