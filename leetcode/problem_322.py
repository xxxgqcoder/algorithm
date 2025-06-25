import unittest
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        # dp[i]: min coins required to make up to amount i using coins
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c < 0:
                    break
                if dp[a - c] == -1:
                    # amout=a-c not reached before, ignore
                    continue
                # use one coin c
                if dp[a] == -1:
                    dp[a] = 1 + dp[a - c]
                else:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount]

    def coinChange_BFS(self, coins: List[int], amount: int) -> int:
        from collections import deque

        q = deque()
        q.append(amount)
        visited = {}
        level = 0

        coins = sorted(coins)
        while len(q) > 0:
            level_size = len(q)

            while level_size > 0:
                # enumerate current level
                level_size -= 1
                current_amt = q.popleft()
                visited[current_amt] = True
                if current_amt == 0:
                    return level

                for c in coins:
                    next_amt = current_amt - c
                    if not visited.get(next_amt, False) and next_amt >= 0:
                        q.append(next_amt)
            level += 1

        return -1


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        coins = [1, 2, 5]
        amount = 11
        expected = 3
        # ret = solution.coinChange(coins, amount)
        ret = solution.coinChange_BFS(coins, amount)
        self.assertEqual(ret, expected)

        # case 2
        coins = [2]
        amount = 3
        expected = -1
        # ret = solution.coinChange(coins, amount)
        ret = solution.coinChange_BFS(coins, amount)
        self.assertEqual(ret, expected)

        # case 3
        coins = [1]
        amount = 0
        expected = 0
        # ret = solution.coinChange(coins, amount)
        ret = solution.coinChange_BFS(coins, amount)
        self.assertEqual(ret, expected)

        # case 4
        coins = [474, 83, 404, 3]
        amount = 264
        expected = 8
        # ret = solution.coinChange(coins, amount)
        ret = solution.coinChange_BFS(coins, amount)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
