from typing import List
import unittest


class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1

        while s[end] == " ":
            end -= 1

        start = end
        while start >= 0 and s[start] != " ":
            start -= 1

        return end - start


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        s = "Hello World"
        expected = 5
        ret = solution.lengthOfLastWord(s)
        self.assertEqual(ret, expected)

        # case 2
        s = "   fly me   to   the moon  "
        expected = 4
        ret = solution.lengthOfLastWord(s)
        self.assertEqual(ret, expected)

        # case 3
        s = "luffy is still joyboy"
        expected = 6
        ret = solution.lengthOfLastWord(s)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
