import unittest
from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        current_comb = [0] * k

        def search(i):
            if i == k:
                ret.append(current_comb[:])
                return
            for num in range(1, n + 1):
                if i > 0 and num <= current_comb[i - 1]:
                    continue
                current_comb[i] = num
                search(i + 1)

        search(0)

        return ret


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        n = 4
        k = 2
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        ret = solution.combine(n, k)
        self.assertEqual(ret, expected)

        # case 2
        n = 1
        k = 1
        expected = [[1]]
        ret = solution.combine(n, k)
        self.assertEqual(ret, expected)

        # case 3
        n = 4
        k = 3
        expected = [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
        ret = solution.combine(n, k)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
