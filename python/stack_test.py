import pytest
import sys

from stack import Element, Stack


def test1():
    stack = Stack(Element(1))
    stack.push(Element(2))
    stack.push(Element(3))

    assert stack.pop().value == 3
    assert stack.pop().value == 2
    assert stack.pop().value == 1
    assert stack.pop() == None

    stack.push(Element(4))
    assert stack.pop().value == 4


if __name__ == "__main__":
    pytest.main(sys.argv)
