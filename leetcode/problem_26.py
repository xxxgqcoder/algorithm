import unittest
from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        i = 0  # the last index of already deduped list
        j = i + 1
        while j < len(nums):
            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            if j < len(nums):
                nums[i + 1] = nums[j]
                i += 1

        return i + 1


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [1, 1, 2]
        expected_nums = [1, 2]
        ret = solution.removeDuplicates(nums)
        self.assertEqual(ret, 2)
        for i in range(ret):
            self.assertEqual(nums[i], expected_nums[i])

        # case 2
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_nums = [0, 1, 2, 3, 4]
        ret = solution.removeDuplicates(nums)
        self.assertEqual(ret, 5)
        for i in range(ret):
            self.assertEqual(nums[i], expected_nums[i])


if __name__ == '__main__':

    unittest.main()
