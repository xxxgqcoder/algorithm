import unittest
from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                # consecutive equal num
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    # need bigger value next iteration
                    j += 1
                elif total > 0:
                    # need smaller value next iteration
                    k -= 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    # move j
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return ret


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [-1, 0, 1, 2, -1, -4]
        want = [[-1, -1, 2], [-1, 0, 1]]
        ret = solution.threeSum(nums)
        self.assertEqual(ret, want)

        # case 2
        nums = [0, 1, 1]
        want = []
        ret = solution.threeSum(nums)
        self.assertEqual(ret, want)

        # case 3
        nums = [0, 0, 0]
        want = [[0, 0, 0]]
        ret = solution.threeSum(nums)
        self.assertEqual(ret, want)


if __name__ == '__main__':
    unittest.main()
