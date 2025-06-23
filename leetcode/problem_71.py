import unittest
from typing import List


class Solution:

    def simplifyPath(self, path: str) -> str:
        stack = []

        def path_elements(path):
            i = 0
            ret = []
            while i < len(path):
                if path[i] == '/':
                    ret.append(path[i])
                    i += 1
                else:
                    j = i
                    while j < len(path) and path[j] != '/':
                        j += 1
                    ret.append(path[i:j])
                    i = j

            return ret

        elements = path_elements(path)

        stack = []
        for e in elements:
            if e == '/':
                while len(stack) > 0 and stack[-1] == '/':
                    stack.pop()
                stack.append(e)
            elif e == '.':
                continue
            elif e == '..':
                while len(stack) > 0 and stack[-1] == '/':
                    stack.pop()
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(e)

        while len(stack) > 0 and stack[-1] == '/':
            stack.pop()
        if len(stack) == 0:
            stack.append('/')
        return "".join(stack)


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # # case 1
        # path = "/home/"
        # expected = "/home"
        # ret = solution.simplifyPath(path)
        # self.assertEqual(ret, expected)

        # # case 2
        # path = "/home//foo/"
        # expected = "/home/foo"
        # ret = solution.simplifyPath(path)
        # self.assertEqual(ret, expected)

        # # case 3
        # path = "/home/user/Documents/../Pictures"
        # expected = "/home/user/Pictures"
        # ret = solution.simplifyPath(path)
        # self.assertEqual(ret, expected)

        # # case 4
        # path = "/../"
        # expected = "/"
        # ret = solution.simplifyPath(path)
        # self.assertEqual(ret, expected)

        # # case 5
        # path = "/.../a/../b/c/../d/./"
        # expected = "/.../b/d"
        # ret = solution.simplifyPath(path)
        # self.assertEqual(ret, expected)

        # case 6
        path = "/.."
        expected = '/'
        ret = solution.simplifyPath(path)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
