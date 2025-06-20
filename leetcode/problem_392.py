import unittest
from typing import List


class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        # s is subsequence of t
        m, n = len(s), len(t)
        if m == 0 and n == 0:
            return True
        if n == 0:
            return False
        if m == 0:
            return True

        # dp[i][j]: longest common subsequence of s[0, i] and t[0, j] (range [0, j] includes position j)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # initial case
        if s[0] == t[0]:
            dp[0][0] = 1

        # init i = 0
        for j in range(1, n):
            if s[0] == t[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]

        # init j = 0
        for i in range(1, m):
            if s[i] == t[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]

        # dp
        for i in range(1, m):
            for j in range(1, n):
                if s[i] == t[j]:
                    dp[i][j] = 1 + dp[i - 1][
                        j -
                        1]  # LCS is calculated based on s[0, i-1] and t[0, j-1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1] == m


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        s = "abc"
        t = "ahbgdc"
        expected = True
        ret = solution.isSubsequence(s, t)
        self.assertEqual(ret, expected)

        # case 2
        s = "axc"
        t = "ahbgdc"
        expected = False
        ret = solution.isSubsequence(s, t)
        self.assertEqual(ret, expected)

        # case 3
        s = ""
        t = "ahbgdc"
        expected = True
        ret = solution.isSubsequence(s, t)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
