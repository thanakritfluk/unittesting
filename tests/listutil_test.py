import unittest
from listutil import count_unique


class TestCountUnique(unittest.TestCase):

    def test_empty_list(self):
        list = []
        self.assertEquals(0, count_unique(list))

    def test_everything_unique(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(5, count_unique(list))
        list = ['a', 'b', 'c']
        self.assertEqual(3, count_unique(list))

    def test_same_all_element(self):
        list = ['a', 'a', 'a']
        self.assertEqual(1, count_unique(list))
        list = [1, 1, 1]
        self.assertEqual(1, count_unique(list))


    def test_too_many_element(self):
        list = []
        for i in range (1,100000):
            list.append(i)
        self.assertEqual(99999,count_unique(list))


    def test_one_element(self):
        list = ['a']
        self.assertEqual(1, count_unique(list))
        list = [1]
        self.assertEqual(1, count_unique(list))


# class TestBinarySearch(unittest.TestCase):
#
#     def test_same(self):
#         list = ['a']
