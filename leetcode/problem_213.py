import unittest
from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        def rob_range(i, j):
            if j - i + 1 <= 2:
                return max(nums[i:j + 1])

            dp = [0] * (j - i + 1)
            dp[0] = nums[i]
            dp[1] = max(nums[i], nums[i + 1])
            for k in range(2, j - i + 1):
                dp[k] = max(dp[k - 1], dp[k - 2] + nums[k + i])
            return dp[-1]

        return max(rob_range(0, len(nums) - 2), rob_range(1, len(nums) - 1))


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # # case 1
        nums = [2, 3, 2]
        expected = 3
        ret = solution.rob(nums)
        self.assertEqual(ret, expected)

        # case 1
        nums = [1, 2, 3, 1]
        expected = 4
        ret = solution.rob(nums)
        self.assertEqual(ret, expected)

        # case 3
        nums = [1, 2, 3]
        expected = 3
        ret = solution.rob(nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
