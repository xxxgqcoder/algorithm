from typing import List
import unittest


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, left, right):
            i, j = left, right
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if len(nums) < 2:
            return
        k = k % len(nums)
        # step 1: reverse [len(nums) - k, len(nums) - 1]
        reverse(nums, len(nums) - k, len(nums) - 1)

        # step 2: reverse [0, len(nums) - k - 1]
        reverse(nums, 0, len(nums) - k - 1)

        # step 3: reverse whole list
        reverse(nums, 0, len(nums) - 1)


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [5, 6, 7, 1, 2, 3, 4]
        solution.rotate(nums, k)
        for i in range(len(nums)):
            self.assertEqual(nums[i], expected[i])

        # case 2
        nums = nums = [-1, -100, 3, 99]
        k = 2
        expected = [3, 99, -1, -100]
        solution.rotate(nums, k)
        for i in range(len(nums)):
            self.assertEqual(nums[i], expected[i])

        # case 3
        nums = [1, 2, 3, 4, 5, 6]
        k = 11
        expected = [2, 3, 4, 5, 6, 1]
        solution.rotate(nums, k)
        for i in range(len(nums)):
            self.assertEqual(nums[i], expected[i])


if __name__ == '__main__':
    unittest.main()
