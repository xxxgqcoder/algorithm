import unittest
from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        i = -1  # index of last element
        j = 0
        while j < len(nums):
            while j < len(nums) and nums[j] == val:
                j += 1
            if j < len(nums):
                nums[i + 1] = nums[j]
                i += 1
                j += 1

        return i + 1


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [3, 2, 2, 3]
        val = 3
        expected_nums = [2, 2]
        ret = solution.removeElement(nums=nums, val=val)
        self.assertEqual(ret, 2)
        for i in range(ret):
            self.assertEqual(nums[i], expected_nums[i])

        # case 2
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_nums = [0, 1, 3, 0, 4]

        ret = solution.removeElement(nums=nums, val=val)

        self.assertEqual(ret, 5)
        for i in range(ret):
            self.assertEqual(nums[i], expected_nums[i])

        # case 3
        nums = [1, 1]
        val = 1
        expected_nums = []

        ret = solution.removeElement(nums=nums, val=val)
        self.assertEqual(ret, 0)
        for i in range(ret):
            self.assertEqual(nums[i], expected_nums[i])


if __name__ == '__main__':

    unittest.main()
