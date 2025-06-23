from typing import List
import unittest


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index = {}
        for i, num in enumerate(nums):
            if num in num_index:
                idx = num_index[num]
                if i - idx <= k:
                    return True
            num_index[num] = i

        return False


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        nums = [1, 2, 3, 1]
        k = 3
        expected = True
        ret = solution.containsNearbyDuplicate(nums, k)
        self.assertEqual(ret, expected)

        # case 2
        nums = [1, 0, 1, 1]
        k = 1
        expected = True
        ret = solution.containsNearbyDuplicate(nums, k)
        self.assertEqual(ret, expected)

        # case 3
        nums = [1, 2, 3, 1, 2, 3]
        k = 2
        expected = False
        ret = solution.containsNearbyDuplicate(nums, k)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
