import unittest
from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                # loosen goal to left using a greedy strategy
                goal = i

        return True if goal == 0 else False


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        nums = [2, 3, 1, 1, 4]
        expected = True
        ret = solution.canJump(nums)
        self.assertEqual(ret, expected)

        # case 2
        nums = [3, 2, 1, 0, 4]
        expected = False
        ret = solution.canJump(nums)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
