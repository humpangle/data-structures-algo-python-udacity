import pytest
import sys

from linked_list import Element, LinkedList


def test_1():
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    assert ll.get_position(3).value == 3
    assert ll.head.next.next.value == 3

    ll.insert(e4, 3)
    assert ll.get_position(3).value == 4

    ll.delete(1)
    assert ll.get_position(1).value == 2

    lx = LinkedList()
    lx.delete(1)
    assert lx.head == None

    lx.append(Element(1))
    lx.delete(1)
    assert lx.head == None

    lx.append(e1)
    lx.delete(2)
    assert lx.head.value == 1

    ly = LinkedList()
    ly.append(Element(1))
    ly.append(Element(2))
    assert ly.head.next.value == 2
    ly.delete(2)
    assert ly.head.next == None

    ly = LinkedList()
    ly.append(Element(1))
    ly.append(Element(2))
    ly.append(Element(3))
    ly.append(Element(4))
    ly.append(Element(5))
    assert ly.get_position(3).value == 3
    ly.delete(3)
    assert ly.get_position(3).value == 4

    l1 = LinkedList()
    assert l1.head == None
    l1.insert(e1, 20)
    assert l1.head == e1
    l1.insert(e2, 1)
    assert l1.head == e2
    assert l1.get_position(1).value == 2
    assert l1.get_position(2).value == 1
    l1.insert(e3, 2)
    assert l1.get_position(2).value == 3


if __name__ == "__main__":
    pytest.main(sys.argv)
