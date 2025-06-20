from typing import List
import unittest


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_index = {}
        for i, num in enumerate(numbers):
            remain = target - num
            if remain in num_index:
                return [num_index[remain], i + 1]
            num_index[num] = i + 1

        return [-1, -1]


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]
        ret = solution.twoSum(numbers, target)
        self.assertEqual(ret, expected)

        # case 2
        numbers = [2, 3, 4]
        target = 6
        expected = [1, 3]

        ret = solution.twoSum(numbers, target)
        self.assertEqual(ret, expected)

        # case 3
        numbers = [-1, 0]
        target = -1
        expected = [1, 2]
        ret = solution.twoSum(numbers, target)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
