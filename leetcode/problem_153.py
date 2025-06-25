import unittest
from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            # donot use <= for the loop condition
            # left <= mid < right
            mid = (left + right) // 2

            # suppose index of miminum value is pivot
            if nums[mid] > nums[right]:
                # case: [left, ..., mid, ..., pivot, ..., right]
                # mid appears to the left of p
                # since nums are rotated sorted array, nums[left] >= nums[right]
                # and mid >= left
                left = mid + 1
            else:
                # nums[mid] <= nums[right]
                # case: [left, ...., pivot, ..., mid, ..., right]
                # mid < right so mid may store a value at least less than right and
                # maybe the minimum value
                right = mid

        # loop ends when left == right
        # from last while loop,
        # if left increase, increased left satisfy nums[left] >= nums[piviot]
        # if right decrease, decreased right satisfy nums[right] >= nums[pivot]
        # now left == right, which means nums[left] == nums[right] == nums
        return nums[left]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [3, 4, 5, 1, 2]
        expected = 1
        ret = solution.findMin(nums)
        self.assertEqual(ret, expected)

        # case 2
        nums = [4, 5, 6, 7, 0, 1, 2]
        expected = 0
        ret = solution.findMin(nums)
        self.assertEqual(ret, expected)

        # case 3
        nums = [11, 13, 15, 17]
        expected = 11
        ret = solution.findMin(nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
