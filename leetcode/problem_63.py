import unittest
from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m < 1:
            return -1
        n = len(obstacleGrid[0])
        if n < 1:
            return -1

        # dp[i][j]: unique path to point (i, j)
        dp = [[-1] * n for _ in range(m)]
        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        # first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j - 1]
        # first col
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i - 1][0]

        # dp
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        obstacleGrid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        expected = 2
        ret = solution.uniquePathsWithObstacles(obstacleGrid)
        self.assertEqual(ret, expected)

        # case 2
        obstacleGrid = [
            [0, 1],
            [0, 0],
        ]
        expected = 1
        ret = solution.uniquePathsWithObstacles(obstacleGrid)
        self.assertEqual(ret, expected)

        # case 3
        obstacleGrid = [[1]]
        expected = 0
        ret = solution.uniquePathsWithObstacles(obstacleGrid)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
