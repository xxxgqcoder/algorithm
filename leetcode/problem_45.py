import unittest
from typing import List


class Solution:

    def jump(self, nums: List[int]) -> bool:
        # dp[i]: min step to reach last index from index i
        n = len(nums)
        dp = [float('inf')] * n
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if i + nums[i] >= j:
                    # can jump to j from i
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[0]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        nums = [2, 3, 1, 1, 4]
        expected = 2
        ret = solution.jump(nums)
        self.assertEqual(ret, expected)

        # case 2
        nums = [2, 3, 0, 1, 4]
        expected = 2
        ret = solution.jump(nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
