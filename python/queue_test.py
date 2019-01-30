import pytest
import sys

from queue import Queue


def test1():
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert q.peek() == 1
    assert q.dequeue() == 1

    q.enqueue(4)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4

    q.enqueue(5)
    assert q.peek() == 5


if __name__ == "__main__":
    pytest.main(sys.argv)
