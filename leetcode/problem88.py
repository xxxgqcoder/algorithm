from typing import List
import unittest


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        p = len(nums1) - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p1 >= 0:
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        return nums1


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        m, n = 3, 3
        ret = solution.merge(nums1, m, nums2, n)
        self.assertEqual(ret, [1, 2, 2, 3, 5, 6])


if __name__ == '__main__':
    unittest.main()