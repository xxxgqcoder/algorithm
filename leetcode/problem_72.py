import unittest
from typing import List


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # dp[i][j]: min step required to transform from word1[:i] to word2[:j]
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = 0

        # first row
        for j in range(1, n + 1):
            # word1 is empty
            # can always transform to word2 by inserting ending character of word2[:j]
            dp[0][j] = dp[0][j - 1] + 1
        # first col
        for i in range(1, m + 1):
            # word2 is empty
            # can always transform to word2 by deleting ending character of word1[:i]
            dp[i][0] = dp[i - 1][0] + 1

        # dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # word1 [0, ..., i]
                # word2 [0, ..., j]
                if word1[i - 1] == word2[j - 1]:
                    # no operation required
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # dp[i-1][j] -> dp[i][j]
                    # delete word1[i-1]
                    delete = 1 + dp[i - 1][j]

                    # dp[i][j-1] -> dp[i][j]
                    # insert word1[i-1]
                    insert = 1 + dp[i][j - 1]

                    # dp[i-1][j-1] -> dp[i][j]
                    # replace word1[i-1] with word2[j-1]
                    replace = 1 + dp[i - 1][j - 1]
                    dp[i][j] = min(delete, insert, replace)

        return dp[m][n]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        word1 = "horse"
        word2 = "ros"
        expected = 3
        ret = solution.minDistance(word1, word2)
        self.assertEqual(ret, expected)

        # case 1
        word1 = "intention"
        word2 = "execution"
        expected = 5
        ret = solution.minDistance(word1, word2)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
