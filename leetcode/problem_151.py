import unittest
from typing import List


class Solution:

    def reverseWords(self, s: str) -> str:
        words = []
        n = len(s)
        i = 0
        while i < n:
            # find first non-space character
            while i < n and s[i] == ' ':
                i += 1

            # find next space
            j = i
            while j < n and s[j] != ' ':
                j += 1

            if j > i:
                words.append(s[i:j])

            # for next iteration
            i = j

        # reverse word
        i, j = 0, len(words) - 1
        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1

        return " ".join(words)


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        s = "the sky is blue"
        expected = "blue is sky the"
        ret = solution.reverseWords(s)
        self.assertEqual(ret, expected)

        # case 2
        s = "  hello world  "
        expected = "world hello"
        ret = solution.reverseWords(s)
        self.assertEqual(ret, expected)

        # case 3
        s = "a good   example"
        expected = "example good a"
        ret = solution.reverseWords(s)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
