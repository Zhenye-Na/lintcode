from collections import deque


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here
        # Bidirectional BFS
        if start == end:
            return 1

        q1, q2 = deque([start]), deque([end])
        s1, s2 = set([start]), set([end])
        step = 1

        while q1 or q2:
            step += 1
            for _ in range(len(q1)):
                word = q1.popleft()
                for next_word in self.get_next_words(word):
                    # same as in normal BFS
                    if next_word not in dict or next_word in s1:
                        continue
                    if next_word in s2:  # start BFS connected end BFS
                        return step

                    s1.add(next_word)
                    q1.append(next_word)

            step += 1
            for _ in range(len(q2)):
                word = q2.popleft()
                for next_word in self.get_next_words(word):

                    # same as in normal BFS
                    if next_word not in dict or next_word in s2:
                        continue
                    if next_word in s1:  # start BFS connected end BFS
                        return step

                    s2.add(next_word)
                    q2.append(next_word)

        return 0

    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words
