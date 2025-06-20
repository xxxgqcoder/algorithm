import unittest
from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        from functools import cmp_to_key

        def compare(a, b):
            if len(a) == len(b):
                if a < b:
                    return -1
                elif a == b:
                    return 0
                else:
                    return 1
            else:
                return -1 if len(a) < len(b) else 1

        strs.sort(key=cmp_to_key(compare))

        pref = strs[0]
        for i in range(1, len(strs)):
            if len(pref) == 0:
                break
            s = strs[i]

            if pref == s[0:len(pref)]:
                continue
            else:
                while len(pref) > 0 and pref != s[:len(pref)]:
                    pref = pref[:-1]

        return pref


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        strs = ["flower", "flow", "flight"]
        expected = 'fl'
        ret = solution.longestCommonPrefix(strs)
        self.assertEqual(ret, expected)

        # case 2
        strs = ["dog", "racecar", "car"]
        expected = ""

        ret = solution.longestCommonPrefix(strs)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
