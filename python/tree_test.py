import pytest
import sys

from tree import Queue


def test1():
    q = Queue()
    assert q.size() == 0

    q.enqueue(1)
    assert q.size() == 1
    q.enqueue(2)
    assert q.size() == 2
    q.enqueue(3)
    assert q.size() == 3
    assert q.dequeue() == 1
    assert q.size() == 2
    assert q.dequeue() == 2
    assert q.size() == 1
    assert q.dequeue() == 3
    assert q.size() == 0
    assert q.dequeue() == None  # NOQA: E711
    assert q.size() == 0


if __name__ == "__main__":
    pytest.main(sys.argv)
