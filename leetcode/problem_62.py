import unittest
from typing import List


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        if m < 1 or n < 1:
            return 0

        # dp[i][j]: unique path to reach (i,j) from (0,0)
        dp = [[1] * n for _ in range(m)]
        # intial case
        # dp[0][0]: 1 path to reach (0,0)
        # first row: dp[0][:], 1 path to reach point in first row
        # first col: dp[:][0], 1 path to reach point in first col

        # dp
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        m = 3
        n = 7
        expected = 28
        ret = solution.uniquePaths(m, n)
        self.assertEqual(ret, expected)

        # case 2
        m = 3
        n = 2
        expected = 3
        ret = solution.uniquePaths(m, n)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
