from typing import List
import unittest


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])

        return profit


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7
        ret = solution.maxProfit(prices)
        self.assertEqual(ret, expected)

        # case 2
        prices = [1, 2, 3, 4, 5]
        expected = 4
        ret = solution.maxProfit(prices)
        self.assertEqual(ret, expected)

        # case 3
        prices = [7, 6, 4, 3, 1]
        expected = 0
        ret = solution.maxProfit(prices)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
