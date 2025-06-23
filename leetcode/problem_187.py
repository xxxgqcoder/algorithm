from typing import List
import unittest


class Solution:

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq_len = 10
        ret = []
        seq_counter = {}
        for i in range(0, len(s) - seq_len + 1):
            seq = s[i:i + seq_len]
            if seq_counter.get(seq) == 1:
                ret.append(seq)
            seq_counter[seq] = seq_counter.get(seq, 0) + 1

        return ret


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()

        # case 1
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        expected = ["AAAAACCCCC", "CCCCCAAAAA"]
        ret = solution.findRepeatedDnaSequences(s)
        self.assertEqual(ret, expected)

        # case 2
        s = "AAAAAAAAAAAAA"
        expected = ["AAAAAAAAAA"]
        ret = solution.findRepeatedDnaSequences(s)
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
