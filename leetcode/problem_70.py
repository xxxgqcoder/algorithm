import unittest
from typing import List


class Solution:

    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        n = 3
        expected = 3
        ret = solution.climbStairs(n)
        self.assertEqual(ret, expected)

        # case 2
        n = 1
        expected = 1
        ret = solution.climbStairs(n)
        self.assertEqual(ret, expected)

        # case 3
        n = 2
        expected = 2
        ret = solution.climbStairs(n)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
