import unittest
from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        for i in range(len(nums) - 3):
            # skip duplicated starting element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                # skip duplicated starting element.
                # if j = i + 1, it means a new iteration, should not skip
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                t = len(nums) - 1
                while k < t:
                    four_sum = nums[i] + nums[j] + nums[k] + nums[t]

                    if four_sum == target:
                        ret.append([nums[i], nums[j], nums[k], nums[t]])

                        # skip duplicated elements
                        k = k + 1
                        while k < t and nums[k] == nums[k - 1]:
                            k += 1

                        t = t - 1
                        while k < t and nums[t] == nums[t + 1]:
                            t -= 1
                    elif four_sum < target:
                        k += 1  # need bigger value
                    else:
                        t -= 1  # need smaller value

        return ret


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        want = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        ret = solution.fourSum(nums, target)
        self.assertEqual(ret, want)

        # case 2
        nums = [2, 2, 2, 2, 2]
        target = 8
        want = [[2, 2, 2, 2]]
        ret = solution.fourSum(nums, target)
        self.assertEqual(ret, want)


if __name__ == '__main__':

    unittest.main()
