from typing import List
import unittest


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        max_cnt = -1
        val_cnt = {}
        majority = None

        for v in nums:
            if v not in val_cnt:
                val_cnt[v] = 0
            val_cnt[v] += 1
            if val_cnt[v] > max_cnt:
                max_cnt = val_cnt[v]
                majority = v

        return majority


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        nums = [3, 2, 3]
        want = 3
        ret = solution.majorityElement(nums)
        self.assertEqual(ret, want)

        # case 2
        nums = [2, 2, 1, 1, 1, 2, 2]
        want = 2
        ret = solution.majorityElement(nums)
        self.assertEqual(ret, want)


if __name__ == '__main__':
    unittest.main()
