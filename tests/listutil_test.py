import unittest
from listutil import count_unique, binary_search


class TestCountUnique(unittest.TestCase):

    def test_empty_list(self):
        list = []
        self.assertEquals(count_unique(list), 0)

    def test_everything_unique(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(count_unique(list), 5)
        list = ['a', 'b', 'c']
        self.assertEqual(count_unique(list), 3)

    def test_same_all_element(self):
        list = ['a', 'a', 'a']
        self.assertEqual(count_unique(list), 1)
        list = [1, 1, 1]
        self.assertEqual(count_unique(list), 1)

    def test_too_many_element(self):
        list = []
        for i in range(1, 100000):
            list.append(i)
        self.assertEqual(count_unique(list), 99999)

    def test_one_element(self):
        list = ['a']
        self.assertEqual(count_unique(list), 1)
        list = [1]
        self.assertEqual(count_unique(list), 1)


class TestBinarySearch(unittest.TestCase):

    def test_normal_search(self):
        list = ['a', 'a', 'b']
        self.assertEqual(binary_search(list, 'a'), 1)
        list = [1, 1, 2]
        self.assertEqual(binary_search(list, 1), 1)

    def test_not_found(self):
        list = [1, 2, 3, 5]
        self.assertEqual(binary_search(list, 4), -1)

    def test_none_element(self):
        list = None
        self.assertRaises(TypeError)

    def test_large_list(self):
        list = []
        pick = 546
        for i in range(1, 1000):
            list.append(i)
        self.assertEqual(binary_search(list, 546), 545)


if __name__ == "__main__":
    unittest.main()
