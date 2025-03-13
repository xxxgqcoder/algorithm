import unittest

from .search import binary_search


class SearchTest(unittest.TestCase):

    def test_search(self):
        # case 1: 1 elemenet list
        a = [2]
        x = 2
        ret = binary_search(a, x)
        self.assertEqual(ret, 0)

        # case 2: found
        a = [0, 1, 2, 3, 4]
        x = 2
        ret = binary_search(a, x)
        self.assertEqual(ret, 2)

        # case 3: exceed right
        a = [0, 1, 2, 3, 4]
        x = 5
        ret = binary_search(a, x)
        self.assertEqual(ret, -1)

        # case 3: exceed left
        a = [0, 1, 2, 3, 4]
        x = -1
        ret = binary_search(a, x)
        self.assertEqual(ret, -1)


if __name__ == '__main__':
    unittest.main()
