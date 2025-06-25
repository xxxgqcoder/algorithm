import unittest
from typing import List


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)  # rows
        if m < 1:
            return -1
        n = len(grid[0])  # cols
        if n < 1:
            return -1

        # dp[i][j]: minimum path sum to point (i,j)
        dp = [[-1] * (n) for _ in range(m)]
        # initial case: first row and first column
        dp[0][0] = grid[0][0]
        # first row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # first col
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # dp
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])

        return dp[m - 1][n - 1]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        grid = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1],
        ]
        expected = 7
        ret = solution.minPathSum(grid)
        self.assertEqual(ret, expected)

        # case 2
        grid = [
            [1, 2, 3],
            [4, 5, 6],
        ]
        expected = 12
        ret = solution.minPathSum(grid)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
