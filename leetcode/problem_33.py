import unittest
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # left part is sorted
                if nums[left] <= target and target <= nums[mid]:
                    # target in left part
                    right = mid - 1
                else:
                    # target not in left part, sub-problem is to search target
                    # in [mid + 1, right], which is a smaller rotated sorted array.
                    left = mid + 1
            else:
                # right part is sorted
                if nums[mid] <= target and target <= nums[right]:
                    # target in right part
                    left = mid + 1
                else:
                    # target not in right part, sub-problem is to search target
                    # in [left, mid - 1], which is a smaller rotated sorted array.
                    right = mid - 1

        return -1


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        want = 4
        ret = solution.search(nums, target)
        self.assertEqual(ret, want)

        # case 2
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        want = -1
        ret = solution.search(nums, target)
        self.assertEqual(ret, want)

        # case 3
        nums = [1]
        target = 0
        want = -1
        ret = solution.search(nums, target)
        self.assertEqual(ret, want)


if __name__ == '__main__':
    unittest.main()
