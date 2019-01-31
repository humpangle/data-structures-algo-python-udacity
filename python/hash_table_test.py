import pytest
import sys

from hash_table import HashTable


def test1():
    hash_table = HashTable()

    assert hash_table.calculate_hash_value('UDACITY') == 8568
    assert hash_table.lookup('UDACITY') == -1

    hash_table.store('UDACITY')
    assert hash_table.lookup('UDACITY') == 8568

    hash_table.store('UDACIOUS')
    assert hash_table.lookup('UDACIOUS') == 8568


if __name__ == "__main__":
    pytest.main(sys.argv)
