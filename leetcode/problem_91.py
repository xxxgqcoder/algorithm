import unittest
from typing import List


class Solution:

    def numDecodings(self, s: str) -> int:
        if len(s) < 1:
            return 0

        # dp[i]: unique ways to decode string s[0, ..., i], s[i] included
        dp = [0] * len(s)
        # initial case: at most one way to decode one character
        dp[0] = 0 if ord(s[0]) == ord('0') else 1

        # dp
        for i in range(1, len(s)):
            # one digit
            one_digit = ord(s[i]) - ord('0')
            two_digit = 10 * (ord(s[i - 1]) - ord('0')) + one_digit
            way_to_decode = 0
            if 1 <= one_digit and one_digit <= 9:
                way_to_decode += dp[i - 1]
            if 10 <= two_digit and two_digit <= 26:
                way_to_decode += dp[i - 2] if i - 2 >= 0 else 1

            dp[i] = way_to_decode

        return dp[len(s) - 1]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        s = '12'
        expected = 2
        ret = solution.numDecodings(s)
        self.assertEqual(ret, expected)

        # case 2
        s = "226"
        expected = 3
        ret = solution.numDecodings(s)
        self.assertEqual(ret, expected)

        # case 3
        s = "06"
        expected = 0
        ret = solution.numDecodings(s)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
