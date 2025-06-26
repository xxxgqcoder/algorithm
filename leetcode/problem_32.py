import unittest
from typing import List


class Solution:

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 1:
            return 0

        # dp[i]: longest valid parentheses ending with s[i]
        dp = [0] * (n + 1)
        # initial case: dp[0] = 0, s[0] cannot form a valid parenthese

        # dp
        max_len = 0
        for i in range(1, n):
            if s[i] == '(':
                # impossible to form valid parenthese with ending character '('
                dp[i] = 0
                continue

            # s[i] == ')'
            if s[i - 1] == '(':
                # s[i-1, i] = "()"
                dp[i] = dp[i - 2] + 2 if i - 2 >= 0 else 2
                max_len = max(max_len, dp[i])
                continue

            # s[i-1, i] = "))"
            # start index of longest valid paraenthese ending with s[i-1]: i - dp[i-1]
            # one index left: i - 1 - dp[i-1]
            # check left most index
            left_most = i - 1 - dp[i - 1]
            if left_most < 0 or s[left_most] != '(':
                dp[i] = 0
            else:
                dp[i] = dp[i - 1] + 2
                if left_most > 0:
                    dp[i] += dp[left_most - 1]

            max_len = max(max_len, dp[i])

        return max_len


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # # case 1
        # s = "(()"
        # expected = 2
        # ret = solution.longestValidParentheses(s)
        # self.assertEqual(ret, expected)

        # # case 2
        # s = ")()())"
        # expected = 4
        # ret = solution.longestValidParentheses(s)
        # self.assertEqual(ret, expected)

        # # case 3
        # s = ""
        # expected = 0
        # ret = solution.longestValidParentheses(s)
        # self.assertEqual(ret, expected)

        # # case 4
        # s = ")("
        # expected = 0
        # ret = solution.longestValidParentheses(s)
        # self.assertEqual(ret, expected)

        # case 5
        s = "()(())"
        expected = 6
        ret = solution.longestValidParentheses(s)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
    # s = "()(())"
    # solution = Solution()
    # ret = solution.longestValidParentheses(s)
