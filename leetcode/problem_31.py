import unittest
from typing import List


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find first decreasing element from right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            nums.reverse()
            return
        # i points to the first decreasing element
        # find smallest element greater than first decreasing element from right
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [1, 2, 3]
        want = [1, 3, 2]
        solution.nextPermutation(nums)
        self.assertEqual(nums, want)

        # case 2
        nums = [1, 2]
        want = [2, 1]
        solution.nextPermutation(nums)
        self.assertEqual(nums, want)

        # case 3
        nums = [3, 2, 1]
        want = [1, 2, 3]
        solution.nextPermutation(nums)
        self.assertEqual(nums, want)

        # case 4
        nums = [1, 1, 5]
        want = [1, 5, 1]
        solution.nextPermutation(nums)
        self.assertEqual(nums, want)

        # case 4
        nums = [1, 1, 1]
        want = [1, 1, 1]
        solution.nextPermutation(nums)
        self.assertEqual(nums, want)

        # case 5
        nums = [1, 3, 2]
        want = [2, 1, 3]
        solution.nextPermutation(nums)
        self.assertEqual(nums, want)


if __name__ == '__main__':
    unittest.main()
