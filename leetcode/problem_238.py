from typing import List
import unittest


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # perform multiply
        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]

        return nums


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        ret = solution.productExceptSelf(nums)
        self.assertEqual(ret, expected)

        # case 2
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        ret = solution.productExceptSelf(nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
