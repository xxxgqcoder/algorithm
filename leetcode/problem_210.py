import unittest
from typing import List


class Solution:

    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        import queue
        degree = [0] * numCourses
        q = queue.Queue()

        # build graph
        graph = [[] for _ in range(numCourses)]
        for p in prerequisites:
            # p1 is prerequisite of p0
            # p1 -> p0
            graph[p[1]].append(p[0])
            degree[p[0]] += 1

        # put all nodes with zero in-degree to queue
        for node, d in enumerate(degree):
            if d == 0:
                q.put(node)

        # get sort order
        ret = []
        while not q.empty():
            node = q.get()
            ret.append(node)
            for n in graph[node]:
                degree[n] -= 1
                if degree[n] == 0:
                    q.put(n)
        if len(ret) == numCourses:
            return ret
        return []

    def findOrderDFS(self, numCourses: int,
                     prerequisites: List[List[int]]) -> List[int]:
        # build graph
        graph = [[] for _ in range(numCourses)]
        for p in prerequisites:
            # p1 is prerequisite of p0
            # p1 -> p0
            graph[p[1]].append(p[0])

        # 0: not visited; 1: visiting; 2: visited
        visit = [0] * numCourses
        topo_order = []

        def can_finish(node):
            if visit[node] == 1:
                # node is being used as starting point of other traversal, a cycle detected
                return False
            elif visit[node] == 2:
                # node has been visited in other traversal path, do not re-visit
                return True

            # visiting node
            visit[node] = 1
            for n in graph[node]:
                # do not check visit status here, so traversal can expand to
                # previous visited node
                if not can_finish(n):
                    return False

            visit[node] = 2
            topo_order.append(node)

            return True

        # start dfs
        for node in range(numCourses):
            if visit[node] == 0 and not can_finish(node):
                return []

        topo_order.reverse()
        return topo_order


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = [[0, 1]]
        # ret = solution.findOrder(numCourses, prerequisites)
        ret = solution.findOrderDFS(numCourses, prerequisites)
        flag = False
        for r in expected:
            if r == ret:
                flag = True
        self.assertTrue(flag)

        # case 2
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        expected = [[0, 2, 1, 3], [0, 1, 2, 3]]
        # ret = solution.findOrder(numCourses, prerequisites)
        ret = solution.findOrderDFS(numCourses, prerequisites)
        flag = False
        for r in expected:
            if r == ret:
                flag = True
        self.assertTrue(flag)

        # case 3
        numCourses = 1
        prerequisites = []
        expected = [[0]]
        # ret = solution.findOrder(numCourses, prerequisites)
        ret = solution.findOrderDFS(numCourses, prerequisites)
        flag = False
        for r in expected:
            if r == ret:
                flag = True
        self.assertTrue(flag)

        # case 4
        numCourses = 3
        prerequisites = [[1, 0], [1, 2], [0, 1]]
        expected = [[]]
        # ret = solution.findOrder(numCourses, prerequisites)
        ret = solution.findOrderDFS(numCourses, prerequisites)
        print(ret)
        flag = False
        for r in expected:
            if r == ret:
                flag = True
        self.assertTrue(flag)

        # case 5
        numCourses = 2
        prerequisites = [[0, 1], [1, 0]]
        expected = [[]]
        ret = solution.findOrderDFS(numCourses, prerequisites)
        print(ret)
        flag = False
        for r in expected:
            if r == ret:
                flag = True
        self.assertTrue(flag)


if __name__ == '__main__':

    unittest.main()
