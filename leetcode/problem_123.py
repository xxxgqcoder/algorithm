import unittest
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[k][i]: max profit if complete at most k transactions in range [0, ..., i]
        dp = [[0] * n for i in range(3)]
        # first row, profit is 0 because at most 0 transaction can be made.
        # first col, profit is 0 because you can only buy and sell stock at index=0, no profit

        for k in range(1, 3):
            for i in range(1, n):
                max_profit = 0
                for j in range(0, i):
                    # profit if buy at j and sell at i
                    if j >= 1:
                        profit = prices[i] - prices[j] + dp[k - 1][j - 1]
                    else:
                        profit = prices[i] - prices[j]

                    max_profit = max(
                        # no trade at i
                        dp[k][i - 1],
                        profit,
                        max_profit,
                    )

                dp[k][i] = max_profit

        return dp[2][n - 1]

    def maxProfit_v2(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[k][i]: max profit if complete at most k transactions in range [0, ..., i]
        dp = [[0] * n for i in range(3)]
        # first row, profit is 0 because at most 0 transaction can be made.
        # first col, profit is 0 because you can only buy and sell stock at index=0, no profit

        for k in range(1, 3):
            min_cost = prices[0]
            for i in range(1, n):
                min_cost = min(min_cost, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - min_cost)

        return dp[2][n - 1]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        prices = [3, 3, 5, 0, 0, 3, 1, 4]
        expected = 6
        ret = solution.maxProfit_v2(prices)
        self.assertEqual(ret, expected)

        # case 2
        prices = [1, 2, 3, 4, 5]
        expected = 4
        ret = solution.maxProfit_v2(prices)
        self.assertEqual(ret, expected)

        # case 3
        prices = [7, 6, 4, 3, 1]
        expected = 0
        ret = solution.maxProfit_v2(prices)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
