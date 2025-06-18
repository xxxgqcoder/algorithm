import unittest
from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                # search right
                left = mid + 1
            elif nums[mid] > target:
                # search left
                right = mid - 1
            else:
                # found
                return mid
        # when loop ends, left > right and left is calculated by mid + 1.
        # so mid' = left - 1 and nums[mid'] < target, nums[left] > target
        return left


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        nums = [1, 3, 5, 6]
        target = 5
        want = 2
        ret = solution.searchInsert(nums, target)
        self.assertEqual(ret, want)

        # case 2
        nums = [1, 3, 5, 6]
        target = 2
        want = 1
        ret = solution.searchInsert(nums, target)
        self.assertEqual(ret, want)

        # case 3
        nums = [1, 3, 5, 6]
        target = 7
        want = 4
        ret = solution.searchInsert(nums, target)
        self.assertEqual(ret, want)

        # case 4
        nums = [1, 3]
        target = 2
        want = 1
        ret = solution.searchInsert(nums, target)
        self.assertEqual(ret, want)


if __name__ == '__main__':
    unittest.main()
