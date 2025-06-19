from typing import List
import unittest


class Solution:

    def hIndex(self, citations: List[int]) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """
        citations.sort()
        n = len(citations)
        for i, citation in enumerate(citations):
            if citation >= n - i:
                return n - i

        return 0


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        citations = [3, 0, 6, 1, 5]
        expected = 3
        ret = solution.hIndex(citations)
        self.assertEqual(ret, expected)

        # case 1
        citations = [1, 3, 1]
        expected = 1
        ret = solution.hIndex(citations)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
