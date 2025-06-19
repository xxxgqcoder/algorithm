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


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        ret = solution.maxProfit(prices)
        self.assertEqual(ret, expected)

        # case 2
        prices = [7, 6, 4, 3, 1]
        expected = 0
        ret = solution.maxProfit(prices)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
