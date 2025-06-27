import unittest
from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        # dp[i]: maximum subarray ending with nums[i]
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i] + dp[i - 1]:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i - 1]

            max_sum = max(max_sum, dp[i])

        return max_sum


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        ret = solution.maxSubArray(nums)
        self.assertEqual(ret, expected)

        # case 2
        nums = [1]
        expected = 1
        ret = solution.maxSubArray(nums)
        self.assertEqual(ret, expected)

        # case 2
        nums = [5, 4, -1, 7, 8]
        expected = 23
        ret = solution.maxSubArray(nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
