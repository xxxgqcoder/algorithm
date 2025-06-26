import unittest
from typing import List


class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # dp[k][i]: max profit if complete at most k transactions in range [0, ..., i]
        dp = [[0] * n for i in range(k + 1)]

        if k >= n // 2:
            # greedy
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # dp
        for k in range(1, k + 1):
            min_cost = prices[0]
            for i in range(1, n):
                min_cost = min(min_cost, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - min_cost)

        return dp[k][n - 1]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        k = 2
        prices = [2, 4, 1]
        expected = 2
        ret = solution.maxProfit(k, prices)
        self.assertEqual(ret, expected)

        # case 2
        k = 2
        prices = [3, 2, 6, 5, 0, 3]
        expected = 7
        ret = solution.maxProfit(k, prices)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
