from typing import List
import unittest


class Solution:

    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # loop invarint: min value is in [left, right]
        # initial condition satisfied
        while left < right:
            mid = (left + right) // 2
            # always have left <= mid < right
            # suppose index of minimum value is p
            if nums[mid] > nums[right]:
                # [mid, right] is strictly not sorted
                # case: [left, ..., mid, ..., p, ..., right]
                left = mid + 1
            elif nums[mid] < nums[left]:
                # [left, mid] is strictly not sorted
                # case: [left, ..., p-1, p, p+1, ..., mid, ..., right]
                left += 1
                right = mid
            else:
                # case: nums[left] <= nums[mid] <= nums[right],
                # appear when rorate at position within consecutive equal values of original sorted array
                right -= 1

        return nums[left]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        nums = [1, 3, 5]
        expected = 1
        ret = solution.findMin(nums)
        self.assertEqual(ret, expected)

        # case 2
        nums = [2, 2, 2, 0, 1]
        expected = 0
        ret = solution.findMin(nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
