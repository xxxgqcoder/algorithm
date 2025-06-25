import unittest
from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[-1]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [1, 2, 3, 1]
        expected = 4
        ret = solution.rob(nums)
        self.assertEqual(ret, expected)

        # case 2
        nums = [2, 7, 9, 3, 1]
        expected = 12
        ret = solution.rob(nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
