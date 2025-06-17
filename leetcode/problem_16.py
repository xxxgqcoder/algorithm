import unittest
from typing import List


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closet_sum = float('inf')

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == target:
                    return current_sum

                if abs(current_sum - target) < abs(closet_sum - target):
                    closet_sum = current_sum

                if current_sum < target:
                    # need bigger value
                    j += 1
                else:
                    k -= 1

        return closet_sum


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [-1, 2, 1, -4]
        target = 1
        want = 2
        ret = solution.threeSumClosest(nums, target)
        self.assertEqual(ret, want)

        # case 2
        nums = [0, 0, 0]
        target = 1
        want = 0
        ret = solution.threeSumClosest(nums, target)
        self.assertEqual(ret, want)

        # case
        nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        target = 1
        want = 60
        ret = solution.threeSumClosest(nums, target)
        self.assertEqual(ret, want)


if __name__ == '__main__':

    unittest.main()
