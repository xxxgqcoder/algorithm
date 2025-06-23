import unittest
from typing import List


class Solution:

    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for p in prerequisites:
            # direction: p1 -> p0
            # p1 is prerequisite of p0
            graph[p[1]].append(p[0])

        on_path = [False] * numCourses
        visited = [False] * numCourses

        def can_finish(node):
            if on_path[node]:
                # node has been used as starting point from other traversal,
                # a cycle detected
                return False

            if visited[node]:
                # has been visited
                return True

            visited[node] = True
            on_path[node] = True
            for n in graph[node]:
                if not can_finish(n):
                    return False
            on_path[node] = False
            return True

        for node in range(numCourses):
            if not visited[node] and not can_finish(node):
                return False
        return True


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = True
        ret = solution.canFinish(numCourses, prerequisites)
        self.assertEqual(ret, expected)

        # case 2
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        expected = False
        ret = solution.canFinish(numCourses, prerequisites)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
