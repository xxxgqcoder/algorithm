class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0

        def next_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ret = nums1[p1]
                    p1 += 1
                else:
                    ret = nums2[p2]
                    p2 += 1
            else:
                if p1 < m:
                    ret = nums1[p1]
                    p1 += 1
                else:
                    ret = nums2[p2]
                    p2 += 1
            return ret

        if (m + n) % 2 != 0:
            for _ in range((m + n) // 2 + 1):
                ret = next_min()
        else:
            for _ in range((m + n) // 2):
                ret = next_min()
            next = next_min()
            ret = (ret + next) / 2
        return ret


solution = Solution()
# case 1:
nums1 = [1, 3]
nums2 = [2]
ret = solution.findMedianSortedArrays(nums1, nums2)
print(ret)
