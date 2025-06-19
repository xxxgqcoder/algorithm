import unittest
from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                # loosen goal to left using a greedy strategy
                goal = i

        return True if goal == 0 else False

    def canJump_dp(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i]: can jump to last index at position i
        dp = [False] * n
        dp[n - 1] = True
        for i in range(n - 2, -1, -1):
            if nums[i] <= 0:
                # can never jump to last at i
                dp[i] = False
                continue

            reachable = i + nums[i]
            for j in range(i + 1, reachable + 1):
                if j < n and dp[j]:
                    # can jump to j and then to last
                    dp[i] = True
        return dp[0]

    def canJump_max_reach(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(0, len(nums)):
            if reach < i:
                return False
            reach = max(reach, i + nums[i])

        return True


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        nums = [2, 3, 1, 1, 4]
        expected = True
        # ret = solution.canJump(nums)
        # ret = solution.canJump_dp(nums)
        ret = solution.canJump_max_reach(nums)
        self.assertEqual(ret, expected)

        # case 2
        nums = [3, 2, 1, 0, 4]
        expected = False
        # ret = solution.canJump(nums)
        # ret = solution.canJump_dp(nums)
        ret = solution.canJump_max_reach(nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
