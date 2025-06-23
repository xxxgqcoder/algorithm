import unittest
from typing import List


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_cnt = {}
        for word in words:
            word_cnt[word] = word_cnt.get(word, 0) + 1

        n = len(words)
        word_len = len(words[0])

        def is_concat(sub_str):
            seen = {}
            for i in range(0, len(sub_str), word_len):
                word = sub_str[i:i + word_len]
                seen[word] = seen.get(word, 0) + 1

            if len(seen) != len(word_cnt):
                return False
            for word in word_cnt:
                if word not in seen or word_cnt[word] != seen[word]:
                    return False
            return True

        ret = []
        for i in range(0, len(s) - n * word_len + 1):
            sub_str = s[i:i + word_len * n]
            if is_concat(sub_str):
                ret.append(i)

        return ret


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        expected = [0, 9]
        ret = solution.findSubstring(s, words)
        self.assertEqual(ret, expected)

        # case 2
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]
        expected = []
        ret = solution.findSubstring(s, words)
        self.assertEqual(ret, expected)

        # case 3
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the"]
        expected = [6, 9, 12]
        ret = solution.findSubstring(s, words)
        self.assertEqual(ret, expected)

        # case 4
        s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
        words = ["fooo", "barr", "wing", "ding", "wing"]
        expected = [13]
        ret = solution.findSubstring(s, words)
        self.assertEqual(ret, expected)

        # case 5
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "good"]
        expected = [8]
        ret = solution.findSubstring(s, words)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
