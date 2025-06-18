import unittest
from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # step 1: find target index
        left, right = 0, len(nums) - 1
        target_index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                target_index = mid
                break
            elif nums[mid] > target:
                # target in left part
                right = mid - 1
            else:
                # target in right part
                left = mid + 1

        if target_index == -1:
            return [-1, -1]

        # step 2: search in left part
        left = 0
        while left < target_index and nums[left] != target:
            # all values in left [left, right] <= target
            mid = (left + right) // 2
            if nums[mid] == target:
                # all values in [mid, right] = target
                # move one step for left
                left += 1
            else:
                # all values in [left, mid] < target
                # move bigger step for left
                left = mid + 1
        left_index = left

        # step 3: search in right part
        right = len(nums) - 1
        while target_index < right and nums[right] != target:
            # all values in [left, right] part >= target
            mid = (target_index + right) // 2
            if nums[mid] == target:
                # all values in [left, mid] = target
                right -= 1
            else:
                # all values in [mid, right] > target
                # move bigger step for right
                right = mid - 1
        right_index = right

        return [left_index, right_index]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        want = [3, 4]
        ret = solution.searchRange(nums, target)
        self.assertEqual(ret, want)

        # case 2
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        want = [-1, -1]
        ret = solution.searchRange(nums, target)
        self.assertEqual(ret, want)

        # case 3
        nums = []
        target = 0
        want = [-1, -1]
        ret = solution.searchRange(nums, target)
        self.assertEqual(ret, want)

        # case 4
        nums = [3, 4]
        target = 3
        want = [0, 0]
        ret = solution.searchRange(nums, target)
        self.assertEqual(ret, want)


if __name__ == '__main__':
    unittest.main()
