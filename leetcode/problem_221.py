import unittest
from typing import List


class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m < 1:
            return 0
        n = len(matrix[0])
        if n < 1:
            return 0

        # dp[i][j]: max length of squre that spread from (i, j) to upper left
        dp = [[0] * n for _ in range(m)]
        # dp
        max_len = 0
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == '0':
                    # cannot spread a square from (i,j)
                    continue

                if i == 0 or j == 0:
                    # boundary
                    dp[i][j] = 1 if matrix[i][j] == '1' else 0
                    max_len = max(dp[i][j], max_len)
                    continue

                # you can only spread minimum length of (i,j)'s neighbour
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1],
                                   dp[i - 1][j])
                max_len = max(dp[i][j], max_len)

        return max_len * max_len


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        expected = 4
        ret = solution.maximalSquare(matrix)
        self.assertEqual(ret, expected)

        # case 2
        matrix = [
            ["0", "1"],
            ["1", "0"],
        ]
        expected = 1
        ret = solution.maximalSquare(matrix)
        self.assertEqual(ret, expected)

        # case 3
        matrix = [["0"]]
        expected = 0
        ret = solution.maximalSquare(matrix)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
