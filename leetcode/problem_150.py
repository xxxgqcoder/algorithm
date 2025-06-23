import unittest
from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                right = stack.pop()
                left = stack.pop()
                if t == '+':
                    stack.append(left + right)
                elif t == '-':
                    stack.append(left - right)
                elif t == '*':
                    stack.append(left * right)
                elif t == '/':
                    stack.append(int(left / right))
                else:
                    pass

            else:
                stack.append(int(t))

        return stack[-1]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        tokens = ["2", "1", "+", "3", "*"]
        expected = 9
        ret = solution.evalRPN(tokens)
        self.assertEqual(ret, expected)

        # case 2
        tokens = ["4", "13", "5", "/", "+"]
        expected = 6
        ret = solution.evalRPN(tokens)
        self.assertEqual(ret, expected)

        # case 3
        tokens = [
            "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"
        ]
        expected = 22
        ret = solution.evalRPN(tokens)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
