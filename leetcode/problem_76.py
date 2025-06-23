import unittest
from typing import List


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        i = 0
        j = 0
        # character counter of [i, j]
        counter = {}
        min_str = ""
        t_counter = {}
        for c in t:
            t_counter[c] = t_counter.get(c, 0) + 1

        def contain_least():
            t_cnt = len(t)
            for c, cnt in t_counter.items():
                if counter.get(c, 0) < cnt:
                    return False
            return True

        while j < len(s):
            # adding s[j]
            counter[s[j]] = counter.get(s[j], 0) + 1

            while i <= j and contain_least():
                # shrink [i, j]
                if len(min_str) == 0 or len(s[i:j + 1]) < len(min_str):
                    min_str = s[i:j + 1]

                # delete s[i]
                counter[s[i]] -= 1
                i += 1

            j += 1

        return min_str


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        s = "ADOBECODEBANC"
        t = "ABC"
        expected = "BANC"
        ret = solution.minWindow(s, t)
        self.assertEqual(ret, expected)

        # case 2
        s = "a"
        t = "a"
        expected = "a"
        ret = solution.minWindow(s, t)
        self.assertEqual(ret, expected)

        # case 3
        s = "a"
        t = "aa"
        expected = ""
        ret = solution.minWindow(s, t)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
