import unittest
from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        if len(s) < 2:
            return s in word_set

        # dp[i]: if substring [0, i) (i included) can be concated by word in word_set)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # initial case when s is empty
        for i in range(1, len(s) + 1):
            flag = False
            for j in range(i - 1, -1, -1):
                word = s[j:i]
                if word in word_set and dp[j]:
                    flag = True
                    break

            dp[i] = flag
        return dp[-1]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        s = "leetcode"
        wordDict = ["leet", "code"]
        expected = True
        ret = solution.wordBreak(s, wordDict)
        self.assertEqual(ret, expected)

        # case 2
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        expected = True
        ret = solution.wordBreak(s, wordDict)
        self.assertEqual(ret, expected)

        # case 3
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        expected = False
        ret = solution.wordBreak(s, wordDict)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
