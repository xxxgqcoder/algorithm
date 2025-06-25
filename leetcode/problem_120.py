import unittest
from typing import List


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        max_row_width = len(triangle[-1])
        path_sum = [-1] * max_row_width
        path_sum[0] = triangle[0][0]

        for i in range(1, len(triangle)):
            row_width = len(triangle[i])

            for j in range(row_width - 1, -1, -1):
                if j == row_width - 1:
                    # come from upper left
                    path_sum[j] = triangle[i][j] + path_sum[j - 1]
                elif j > 0:
                    # min of upper and upper left
                    path_sum[j] = triangle[i][j] + min(path_sum[j],
                                                       path_sum[j - 1])
                else:
                    # com from upper
                    path_sum[j] = triangle[i][j] + path_sum[j]

        max_sum = min(path_sum)

        return max_sum


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        triangle = [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3],
        ]
        expected = 11
        ret = solution.minimumTotal(triangle)
        self.assertEqual(ret, expected)

        # case 2
        triangle = [[-10]]
        expected = -10
        ret = solution.minimumTotal(triangle)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
