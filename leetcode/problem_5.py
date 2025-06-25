import unittest
from typing import List


class Solution:

    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        # dp[i][j]: substr [i, j] (both side included) forms a palindrome
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True

        max_str = ""
        for right in range(n):
            for left in range(right):
                if s[left] != s[right]:
                    dp[left][right] = False
                    continue
                if right - left <= 2:
                    # left, right or left, some_char, right
                    dp[left][right] = True
                else:
                    dp[left][right] = dp[left + 1][right - 1]

                if dp[left][right] and right - left + 1 > len(max_str):
                    max_str = s[left:right + 1]

        return max_str


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        s = "babad"
        expected = "bab"
        ret = solution.longestPalindrome(s)
        self.assertEqual(ret, expected)

        # case 2
        s = "cbbd"
        expected = "bb"
        ret = solution.longestPalindrome(s)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
