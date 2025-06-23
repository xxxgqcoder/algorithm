import unittest
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in num_index:
                return [num_index[remain], i]
            num_index[num] = i

        return []


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        ret = solution.twoSum(nums, target)
        self.assertEqual(ret, expected)

        # case 2
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        ret = solution.twoSum(nums, target)
        self.assertEqual(ret, expected)

        # case 3
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        ret = solution.twoSum(nums, target)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
