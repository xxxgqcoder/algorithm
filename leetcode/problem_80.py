from typing import List
import unittest


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        k = 2  # the index to insert number
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [1, 1, 1, 2, 2, 3]
        want = 5
        expected_nums = [1, 1, 2, 2, 3]
        ret = solution.removeDuplicates(nums)
        self.assertEqual(ret, want)
        for i in range(ret):
            self.assertEqual(nums[i], expected_nums[i])

        # case 2
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        want = 7
        expected_nums = [0, 0, 1, 1, 2, 3, 3]
        ret = solution.removeDuplicates(nums)
        self.assertEqual(ret, want)
        for i in range(ret):
            self.assertEqual(nums[i], expected_nums[i])


if __name__ == '__main__':
    unittest.main()
