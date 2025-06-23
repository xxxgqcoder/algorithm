import unittest
from typing import List


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        # index of current sliding window which forms a non-increasing queue
        dq = deque()
        ret = []
        for i in range(len(nums)):
            # poll from front
            while len(dq) > 0 and dq[0] < i - k + 1:
                dq.popleft()

            # pop back to ensure non-increasing
            while len(dq) > 0 and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # push new element
            dq.append(i)

            if i >= k - 1:
                ret.append(nums[dq[0]])

        return ret


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        ret = solution.maxSlidingWindow(nums, k)
        self.assertEqual(ret, expected)

        # case 2
        nums = [1]
        k = 1
        expected = [1]
        ret = solution.maxSlidingWindow(nums, k)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
