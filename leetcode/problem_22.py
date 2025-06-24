import unittest
from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        comb = []
        ret = []

        def backtrack(i, open_cnt, close_cnt):
            if i >= 2 * n:
                ret.append("".join(comb[:]))
            if open_cnt < n:
                comb.append('(')

                backtrack(i + 1, open_cnt + 1, close_cnt)

                comb.pop()
            if close_cnt < open_cnt:
                comb.append(')')

                backtrack(i + 1, open_cnt, close_cnt + 1)

                comb.pop()

        backtrack(0, 0, 0)
        return ret


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        ret = solution.generateParenthesis(n)

        expected = sorted(expected)
        ret = sorted(ret)
        self.assertEqual(ret, expected)

        # case 2
        n = 1
        expected = ['()']
        ret = solution.generateParenthesis(n)

        expected = sorted(expected)
        ret = sorted(ret)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
