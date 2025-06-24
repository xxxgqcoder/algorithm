import unittest
from typing import List


class Solution:

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque

        n = len(board)
        # min_rolls[i]: min rolls required to reach node i
        min_rolls = [-1] * (n * n + 1)

        # node index to be visited next roll, 1 based
        q = deque()

        min_rolls[1] = 0
        q.append(1)  # initial start at node 1

        while len(q) > 0:
            # current node
            x = q.popleft()

            # BFS
            for i in range(1, 7):
                next = x + i
                if next > n * n:
                    break
                # convert next node to row & col index (0-based)
                row = (next - 1) // n
                col = (next - 1) % n
                # check if snake is present
                snake_dst = board[n - 1 - row][(n - 1 - col) if
                                               (row % 2 == 1) else col]
                y = snake_dst if snake_dst > 0 else next

                if y == n * n:
                    return min_rolls[x] + 1
                if min_rolls[y] == -1:
                    # y not visited before
                    min_rolls[y] = min_rolls[x] + 1
                    q.append(y)
                else:
                    # y can be reached from other path, update min required steps
                    min_rolls[y] = min(min_rolls[x] + 1, min_rolls[y])
        return -1


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        board = [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ]
        expected = 4
        ret = solution.snakesAndLadders(board)
        self.assertEqual(ret, expected)

        # case 2
        board = [
            [-1, -1],
            [-1, 3],
        ]
        expected = 1
        ret = solution.snakesAndLadders(board)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
