import unittest
from typing import List


class Solution:

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:

        res = []

        def search_combination(nums, idx, comb, total):
            """
            Args:
            - nums: the numbers
            - idx: current idx to check
            - comb: current combination
            - total: total sum of previous combination
            """
            if total == target:
                # find solution, copy comb
                res.append(comb[:])
                return
            if idx >= len(nums) or total > target:
                return

            # repeat using nums[idx]
            comb.append(nums[idx])
            search_combination(nums, idx, comb, total + nums[idx])

            # remove nums[idx] from comb, search next index
            comb.pop()
            search_combination(nums, idx + 1, comb, total)

        search_combination(candidates, 0, [], 0)

        return res


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        candidates = [2, 3, 6, 7]
        target = 7
        want = [[2, 2, 3], [7]]
        ret = solution.combinationSum(candidates, target)
        self.assertEqual(ret, want)

        # case 2
        candidates = [2, 3, 5]
        target = 8
        want = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        ret = solution.combinationSum(candidates, target)
        self.assertEqual(ret, want)

        # case 3
        candidates = [2]
        target = 1
        want = []
        ret = solution.combinationSum(candidates, target)
        self.assertEqual(ret, want)


if __name__ == '__main__':
    unittest.main()
