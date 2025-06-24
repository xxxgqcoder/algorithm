import unittest
from typing import List


class Solution:

    def minMutation(self, startGene: str, endGene: str,
                    bank: List[str]) -> int:
        from collections import deque
        if startGene == endGene:
            return 0

        gene_bank = set(bank)
        q = deque()
        visited = {}
        q.append(startGene)

        mutate_set = ['A', 'C', 'G', 'T']
        level = 0
        while len(q) > 0:
            level_size = len(q)
            while level_size > 0:
                # visit all node in current level
                level_size -= 1

                gene = q.popleft()
                visited[gene] = True
                if gene == endGene:
                    return level

                gene = list(gene)
                for i, g in enumerate(gene):
                    for mutate in mutate_set:
                        if mutate == g:
                            continue
                        gene[i] = mutate
                        mutate_gene = "".join(gene)
                        if mutate_gene in gene_bank and not visited.get(
                                mutate_gene, False):
                            q.append(mutate_gene)
                        gene[i] = g

            level += 1

        return -1


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = ["AACCGGTA"]
        expected = 1
        ret = solution.minMutation(startGene, endGene, bank)
        self.assertEqual(ret, expected)

        # case 2
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        expected = 2
        ret = solution.minMutation(startGene, endGene, bank)
        self.assertEqual(ret, expected)

        # case 3
        startGene = "AACCGGTT"
        endGene = "AACCGCTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        expected = 2
        ret = solution.minMutation(startGene, endGene, bank)
        self.assertEqual(ret, expected)

        # case 4
        startGene = "AAAAAAAA"
        endGene = "CCCCCCCC"
        bank = [
            "AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC",
            "AACACCCC", "ACCACCCC", "ACCCCCCC", "CCCCCCCA"
        ]
        expected = -1
        ret = solution.minMutation(startGene, endGene, bank)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
