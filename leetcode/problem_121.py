from typing import List
import unittest


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            profit = max(profit, price - buy_price)

        return profit

    def maxProfit_dp(self, prices: List[int]) -> int:
        # max_prices[i]: max prices in range [i, ..., end], i cluded
        max_prices = [0] * len(prices)
        max_prices[-1] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            max_prices[i] = max(prices[i], max_prices[i + 1])

        #
        max_profit = 0
        for i, p in enumerate(prices):
            # buy at i and sell at max prices
            max_profit = max(max_profit, max_prices[i] - p)

        return max_profit


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        # ret = solution.maxProfit(prices)
        ret = solution.maxProfit_dp(prices)
        self.assertEqual(ret, expected)

        # case 2
        prices = [7, 6, 4, 3, 1]
        expected = 0
        # ret = solution.maxProfit(prices)
        ret = solution.maxProfit_dp(prices)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
