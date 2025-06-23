import unittest
from typing import List


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
                return
            # flip O to #
            board[i][j] = '#'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # traverse from boundary O
        for i in range(m):
            for j in range(n):
                if not (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    continue
                dfs(i, j)

        # flip
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
                else:
                    pass


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]
        solution.solve(board)
        self.assertEqual(board, expected)

        # case 2
        board = [["X"]]
        expected = [["X"]]
        solution.solve(board)
        self.assertEqual(board, expected)


if __name__ == '__main__':

    unittest.main()
