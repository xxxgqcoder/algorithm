import unittest
from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == '0':
                return
            if visited[i][j] == 1:
                return
            visited[i][j] = 1
            # upper
            dfs(i - 1, j)
            # low
            dfs(i + 1, j)
            # left
            dfs(i, j - 1)
            # right
            dfs(i, j + 1)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or visited[i][j] == 1:
                    continue
                dfs(i, j)
                cnt += 1
        return cnt


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        expected = 1
        ret = solution.numIslands(grid)
        self.assertEqual(ret, expected)

        # case 2
        grid = grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        expected = 3
        ret = solution.numIslands(grid)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
