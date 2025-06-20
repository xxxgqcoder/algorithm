import unittest
from typing import List


class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        i = 0
        j = 0
        current_sum = 0  # sum from i to j, not initialized yet
        min_len = len(nums) + 1

        while j < len(nums):
            current_sum += nums[j]

            while current_sum >= target:
                min_len = min(min_len, j - i + 1)
                current_sum -= nums[i]
                i += 1

            j += 1

        return 0 if min_len == len(nums) + 1 else min_len


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        expected = 2

        ret = solution.minSubArrayLen(target, nums)
        self.assertEqual(ret, expected)

        # case 2
        target = 4
        nums = [1, 4, 4]
        expected = 1

        ret = solution.minSubArrayLen(target, nums)
        self.assertEqual(ret, expected)

        # case
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = 0

        ret = solution.minSubArrayLen(target, nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
