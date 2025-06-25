import unittest
from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]
            if target == val:
                return True
            elif target < val:
                right = mid - 1
            else:
                left = mid + 1
        return False


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60],
        ]
        target = 3
        expected = True

        ret = solution.searchMatrix(matrix, target)
        self.assertEqual(ret, expected)

        # case 2
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60],
        ]
        target = 13
        expected = False

        ret = solution.searchMatrix(matrix, target)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
