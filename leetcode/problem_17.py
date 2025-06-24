import unittest
from typing import List


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        digit2letter = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': '',
        }

        current_letters = [""] * len(digits)
        ret = []

        def search(i):
            if i == len(digits):
                comb = ''.join(current_letters)
                if len(comb) > 0:
                    ret.append(comb)
                return

            letters = digit2letter[digits[i]]
            for letter in letters:
                current_letters[i] = letter
                search(i + 1)

        search(0)
        return ret


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        ret = solution.letterCombinations(digits)
        self.assertEqual(ret, expected)

        # case 2
        digits = ""
        expected = []
        ret = solution.letterCombinations(digits)
        self.assertEqual(ret, expected)

        # case 3
        digits = "2"
        expected = ["a", "b", "c"]
        ret = solution.letterCombinations(digits)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
