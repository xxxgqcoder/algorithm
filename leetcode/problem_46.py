import unittest
from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        cur = []
        ret = []

        def backtrack(i):
            if i == len(nums):
                ret.append(cur[:])
                return
            for j in range(i, len(nums)):
                # swap i, j
                nums[i], nums[j] = nums[j], nums[i]
                cur.append(nums[i])

                # permutation of nums[i+1:], with leading num = nums[i]
                backtrack(i + 1)

                # restore
                cur.pop()
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return ret


class ProblemTest(unittest.TestCase):

    def test_test(self):

        from functools import cmp_to_key

        def compare(a, b):
            if len(a) != len(b):
                return -1 if len(a) < len(b) else 1

            for i in range(len(a)):
                if a[i] < b[i]:
                    return -1
                elif a[i] > b[i]:
                    return 1
                else:
                    pass
            return 0

        solution = Solution()

        # case 1
        nums = [1, 2, 3]
        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
        expected = sorted(expected, key=cmp_to_key(compare))
        ret = solution.permute(nums)
        ret = sorted(ret, key=cmp_to_key(compare))
        self.assertEqual(ret, expected)

        # case 2
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        expected = sorted(expected, key=cmp_to_key(compare))
        ret = solution.permute(nums)
        ret = sorted(ret, key=cmp_to_key(compare))
        self.assertEqual(ret, expected)

        # case 3
        nums = [1]
        expected = [[1]]
        expected = sorted(expected, key=cmp_to_key(compare))
        ret = solution.permute(nums)
        ret = sorted(ret, key=cmp_to_key(compare))
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
