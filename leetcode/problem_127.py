import unittest
from typing import List


class Solution:

    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        from collections import deque

        word_set = set(wordList)
        q = deque()
        visited = {}
        q.append(beginWord)
        level = 1
        while len(q) > 0:
            level_size = len(q)

            while level_size > 0:
                # enumerate all node in current level
                level_size -= 1
                word = q.popleft()
                if word == endWord:
                    return level

                word = list(word)
                for i, c in enumerate(word):
                    for j in range(0, 26):
                        mutate = chr(j + ord('a'))
                        if mutate == c:
                            continue
                        word[i] = mutate
                        next_word = "".join(word)
                        if next_word in word_set and not visited.get(
                                next_word, False):
                            visited[next_word] = True
                            q.append(next_word)
                        word[i] = c

            level += 1

        return 0


class ProblemTest(unittest.TestCase):

    def test_test(self):
        solution = Solution()
        # case 1
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        expected = 5
        ret = solution.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(ret, expected)

        # case 2
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        expected = 0
        ret = solution.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(ret, expected)


if __name__ == '__main__':

    unittest.main()
    # solution = Solution()
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # expected = 5
    # ret = solution.ladderLength(beginWord, endWord, wordList)
