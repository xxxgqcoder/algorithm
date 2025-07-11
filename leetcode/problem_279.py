import unittest
from typing import List


class Solution:

    def numSquares(self, n: int) -> int:
        # dp[k]: k最小平方数
        # dp[n] = min(1 + dp[n-k]), k: 1 ~ n, k^2 <= n
        if n < 0:
            return -1
        if n <= 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for k in range(3, n + 1):
            min_num = float("inf")
            for t in range(1, k):
                if t * t > k:
                    break
                remain = k - t * t
                if 1 + dp[remain] < min_num:
                    min_num = 1 + dp[remain]
                    dp[k] = min_num

        return dp[n]


class ProblemTest(unittest.TestCase):

    def test_test(self):

        solution = Solution()

        # case 1
        n = 4
        expected = 1
        ret = solution.numSquares(n)
        self.assertEqual(ret, expected)

        # case 2
        n = 9
        expected = 1
        ret = solution.numSquares(n)
        self.assertEqual(ret, expected)

        # case 3
        n = 12  # 4 + 4 + 4
        expected = 3
        ret = solution.numSquares(n)
        self.assertEqual(ret, expected)

        # case 4
        n = 13  # 4 + 9
        expected = 2
        ret = solution.numSquares(n)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
