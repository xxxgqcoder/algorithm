from typing import List
import unittest


class Solution(object):

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        left = 1
        right = len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] < nums[mid]:
                # slope up
                left = mid + 1
            else:
                # slope down
                right = mid - 1

        return -1


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        nums = [1, 2, 3, 1]
        ret = solution.findPeakElement(nums)
        flag = False

        if ret == 0:
            flag = nums[ret] > nums[ret + 1]
        elif ret == len(nums) - 1:
            flag = nums[ret - 1] < nums[ret]
        else:
            flag = nums[ret - 1] < nums[ret] and nums[ret] > nums[ret + 1]
        self.assertTrue(flag)

        # case 1
        nums = [1, 2, 1, 3, 5, 6, 4]
        ret = solution.findPeakElement(nums)
        flag = False

        if ret == 0:
            flag = nums[ret] > nums[ret + 1]
        elif ret == len(nums) - 1:
            flag = nums[ret - 1] < nums[ret]
        else:
            flag = nums[ret - 1] < nums[ret] and nums[ret] > nums[ret + 1]
        self.assertTrue(flag)


if __name__ == '__main__':
    unittest.main()
