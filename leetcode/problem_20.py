import unittest
from typing import List


class Solution:

    def isValid(self, s: str) -> bool:

        def is_pair(a, b):
            if a in ['(', ')']:
                return b == ')' if a == '(' else b == '('
            elif a in ['[', ']']:
                return b == ']' if a == '[' else b == '['
            elif a in ['{', '{']:
                return b == '}' if a == '{' else b == '{'
            else:
                return False

        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c in [')', ']', '}']:
                if len(stack) > 0 and is_pair(stack[-1], c):
                    stack.pop()
                else:
                    stack.append(c)

        return len(stack) == 0


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        s = "()"
        expected = True
        ret = solution.isValid(s)
        self.assertEqual(ret, expected)

        # case 2
        s = "()[]{}"
        expected = True
        ret = solution.isValid(s)
        self.assertEqual(ret, expected)

        # case 3
        s = "(]"
        expected = False
        ret = solution.isValid(s)
        self.assertEqual(ret, expected)

        # case 3
        s = "([])"
        expected = True
        ret = solution.isValid(s)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
