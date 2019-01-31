"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string.
"""


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in
        the table.
        """
        key = self.calculate_hash_value(string)
        if key < 10_000:
            value = self.table[key] or []
            if string not in value:
                value.append(string)
                self.table[key] = value

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise.
        """
        key = self.calculate_hash_value(string)
        if key < 10_000:
            value = self.table[key] or []
            if string in value:
                return key
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calculate a
        hash value from a string."""
        return ord(string[0]) * 100 + ord(string[1])
