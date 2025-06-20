import unittest

from typing import List


class Solution:

    def isPalindrome(self, s: str) -> bool:
        p = ""
        for c in s:
            c = c.lower()
            if c == ' ' or not ((c >= 'a' and c <= 'z') or
                                (c >= '0' and c <= '9')):
                continue
            p += c

        i, j = 0, len(p) - 1
        while i < j:
            if p[i] != p[j]:
                return False
            i += 1
            j -= 1

        return True


class ProblemTest(unittest.TestCase):

    def test_test(self, ):
        solution = Solution()

        # case 1
        s = "A man, a plan, a canal: Panama"
        expected = True
        ret = solution.isPalindrome(s)
        self.assertEqual(ret, expected)

        # case 2
        s = "race a car"
        expected = False
        ret = solution.isPalindrome(s)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
