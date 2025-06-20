import unittest
from typing import List


class Solution:

    def romanToInt(self, s: str) -> int:
        i = 0
        mappings = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = 0
        n = len(s)
        while i < len(s):
            val = mappings[s[i]]
            next_val = None
            if i + 1 < n:
                next_val = mappings[s[i + 1]]

            if next_val is not None and next_val > val:
                total += val * (-1) + next_val
                i += 2
            else:
                total += val
                i += 1

        return total


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        s = 'III'
        expected = 3
        ret = solution.romanToInt(s)
        self.assertEqual(ret, expected)

        # case 2
        s = "LVIII"
        expected = 58
        ret = solution.romanToInt(s)
        self.assertEqual(ret, expected)

        # case 3
        s = "MCMXCIV"
        expected = 1994
        ret = solution.romanToInt(s)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
