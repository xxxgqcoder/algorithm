import unittest
from typing import List


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_cnt = {}
        i = 0
        max_len = 0
        for j in range(len(s)):
            # [i, j] represents the longest sub string without repeating character
            # adding one character
            if s[j] not in char_cnt:
                char_cnt[s[j]] = 0
            char_cnt[s[j]] += 1

            # ensure doesnt adding repeating character
            while i < j and char_cnt[s[j]] >= 2:
                char_cnt[s[i]] -= 1
                i += 1

            # update max sub sequence length
            max_len = max(max_len, j - i + 1)

        return max_len


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        s = "abcabcbb"
        expected = 3
        ret = solution.lengthOfLongestSubstring(s)
        self.assertEqual(ret, expected)

        # case 2
        s = "bbbbb"
        expected = 1
        ret = solution.lengthOfLongestSubstring(s)
        self.assertEqual(ret, expected)

        # case 3
        s = "pwwkew"
        expected = 3
        ret = solution.lengthOfLongestSubstring(s)
        self.assertEqual(ret, expected)

        # case 4
        s = ""
        expected = 0
        ret = solution.lengthOfLongestSubstring(s)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
