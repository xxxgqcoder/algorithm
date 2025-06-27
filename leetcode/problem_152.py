import unittest
from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        r = imax = imin = nums[0]
        for i in range(1, len(nums)):
            candidates = (nums[i], nums[i] * imax, nums[i] * imin)
            imax = max(candidates)
            imin = min(candidates)

            r = max(r, imax)

        return r


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [2, 3, -2, 4]
        expected = 6
        ret = solution.maxProduct(nums)
        self.assertEqual(ret, expected)

        # case 2
        nums = [-2, 0, -1]
        expected = 0
        ret = solution.maxProduct(nums)
        self.assertEqual(ret, expected)

        # case 3
        nums = [-2, 3, -4]
        expected = 24
        ret = solution.maxProduct(nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
