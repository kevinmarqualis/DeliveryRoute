import unittest
import hash_table


class TestHashTable(unittest.TestCase):

    def my_mocked_hashify(self, id):
        return id % 2

    def test_hashify(self):
        self.assertEqual(self.my_mocked_hashify(2), 0)
        self.assertEqual(self.my_mocked_hashify(3), 1)
