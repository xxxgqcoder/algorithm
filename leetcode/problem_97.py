import unittest
from typing import List


class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        t = len(s3)
        if m + n != t:
            return False
        # dp[i][j]: if s3[:i+j] can be formed by interleaving s1[:i] and s2[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # first row
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and (s2[j - 1] == s3[j - 1])
        # first col
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and (s1[i - 1] == s3[i - 1])

        # dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # to form s3[i+j-1], you can either take s1[i-1] from s1
                # or take s2[j-1] from s2
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) \
                        or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[m][n]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        expected = True
        ret = solution.isInterleave(s1, s2, s3)
        self.assertEqual(ret, expected)

        # case 2
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        expected = False
        ret = solution.isInterleave(s1, s2, s3)
        self.assertEqual(ret, expected)

        # case 3
        s1 = ""
        s2 = ""
        s3 = ""
        expected = True
        ret = solution.isInterleave(s1, s2, s3)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
