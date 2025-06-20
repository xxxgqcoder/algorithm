from typing import List
import unittest


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            stop_cnt = 0
            j = i
            current_gas = 0
            while stop_cnt < n:
                current_gas += gas[j % n] - cost[j % n]
                if current_gas < 0:
                    break
                j += 1
                stop_cnt += 1
            if current_gas >= 0:
                # complete one circuit
                return i
            else:
                # stop at j
                if j < n:
                    i = j + 1
                else:
                    # j exceeds n
                    return -1

        return -1


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        expected = 3
        ret = solution.canCompleteCircuit(gas, cost)
        self.assertEqual(ret, expected)

        # case 2
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        expected = -1
        ret = solution.canCompleteCircuit(gas, cost)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
