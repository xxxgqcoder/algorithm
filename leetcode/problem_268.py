import unittest
from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        left = 0
        right = len(nums)
        # loop invariant: [left, right] contains the missing value
        while left < right:
            mid = (left + right) // 2
            if mid == nums[mid]:
                # missing value is in [mid + 1, ]
                left = mid + 1
            elif mid < nums[mid]:
                right = mid
            else:
                # mid > nums[mid]: impossiple
                pass
        return left


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [3, 0, 1]
        expected = 2
        ret = solution.missingNumber(nums)
        self.assertEqual(ret, expected)

        # case 2
        nums = [0, 1]
        expected = 2
        ret = solution.missingNumber(nums)
        self.assertEqual(ret, expected)

        # case 3
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        expected = 8
        ret = solution.missingNumber(nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
