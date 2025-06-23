import unittest
from typing import List


class Solution:

    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int,
                                      valueDiff: int) -> bool:
        # map from bucket index to num
        buckets = {}
        if valueDiff < 0:
            return False

        for i, num in enumerate(nums):
            bucket = num // (valueDiff + 1)  # + 1 to avoid division by zero
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and abs(buckets.get(bucket - 1) -
                                             num) <= valueDiff:
                return True
            if bucket + 1 in buckets and abs(buckets.get(bucket + 1) -
                                             num) <= valueDiff:
                return True

            buckets[bucket] = num

            if i >= indexDiff:
                bucket = nums[i - indexDiff] // (valueDiff + 1)
                del buckets[bucket]

        return False


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        nums = [1, 2, 3, 1]
        indexDiff = 3
        valueDiff = 0
        expected = True
        ret = solution.containsNearbyAlmostDuplicate(nums, indexDiff,
                                                     valueDiff)
        self.assertEqual(ret, expected)

        # case 1
        nums = [1, 5, 9, 1, 5, 9]
        indexDiff = 2
        valueDiff = 3
        expected = False
        ret = solution.containsNearbyAlmostDuplicate(nums, indexDiff,
                                                     valueDiff)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
