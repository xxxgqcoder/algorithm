import unittest
from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, k):
            if k >= len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                # out of board
                return False

            if board[i][j] != word[k]:
                # character doesnt match
                return False

            # mark to avoid revisit
            board[i][j] = '#'

            # dfs visit
            flag = dfs(i+1, j, k+1)\
                    or dfs(i-1, j, k+1) \
                    or dfs(i, j-1, k+1) \
                    or dfs(i, j+1, k+1)
            # restore
            board[i][j] = word[k]

            return flag

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]
        word = "ABCCED"
        expected = True

        ret = solution.exist(board, word)
        self.assertEqual(ret, expected)

        # case 2
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]
        word = "SEE"
        expected = True

        ret = solution.exist(board, word)
        self.assertEqual(ret, expected)

        # case 3
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]
        word = "ABCB"
        expected = False

        ret = solution.exist(board, word)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
