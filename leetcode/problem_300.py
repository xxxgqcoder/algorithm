import unittest
from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]: length of longest subsequence in range [0, i], with ending number being nums[i]
        dp = [1] * len(nums)
        max_len = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    max_len = max(max_len, dp[i])

        return max_len


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expected = 4
        ret = solution.lengthOfLIS(nums)
        self.assertEqual(ret, expected)

        # case 2
        nums = [0, 1, 0, 3, 2, 3]
        expected = 4
        ret = solution.lengthOfLIS(nums)
        self.assertEqual(ret, expected)

        # case 3:
        nums = [7, 7, 7, 7, 7, 7, 7]
        expected = 1
        ret = solution.lengthOfLIS(nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
