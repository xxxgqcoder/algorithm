import unittest

from .problem4 import Solution


class Problem4Test(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1: odd len
        nums1 = [1, 3]
        nums2 = [2]
        ret = solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(ret, 2)

        # case 1: even len
        nums1 = [1, 2]
        nums2 = [3, 4]
        ret = solution.findMedianSortedArrays(nums1, nums2)
        self.assertAlmostEqual(ret, 2.5)


if __name__ == '__main__':
    unittest.main()