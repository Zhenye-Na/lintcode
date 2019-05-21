# 120. Word Ladder

**Description**

Given two words (`start` and `end`), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.

Transformation rule such that:

1. Only *one* letter can be changed at a time
2. Each intermediate word must exist in the dictionary. (`start` and `end` words do not need to appear in the dictionary)

```
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
```

**Example**

Example 1:

```
Input: start = "a"，end = "c"，dict =["a","b","c"]
Output: 2
Explanation:
"a"->"c"
```

Example 2:

```
Input: start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
Output: 5
Explanation
"hit"->"hot"->"dot"->"dog"->"cog"
```

**双向 BFS**

双向BFS: 有点类似于用两个 queue 的 BFS, 从 `start` 开始一个 `queue1`, 从 `end` 开始一个 `queue2`, 然后两边寻找.


```python
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
```


**BFS**

使用 `steps` 这个 `hash` 来存储距离来实现记录每个节点的距离

```python
from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dictionary):
        # write your code here
        if start == end:
            return 1

        dictionary.add(end)
        steps = {start:1}
        queue = deque([start])

        while queue:
            word = queue.popleft()
            if word == end:
                return steps[word]

            for candidate in self._next_words(word):

                if candidate not in dictionary or candidate in steps:
                    continue

                queue.append(candidate)
                steps[candidate] = steps[word] + 1
 
        return 0

    # O(26 * L^2)
    # L is the length of word
    def _next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words
```


分层遍历

```python
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([start])
        visited = set([start])
        
        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance
                
                for next_word in self.get_next_words(word):
                    if next_word not in dict or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word) 

        return 0
        
    # O(26 * L^2)
    # L is the length of word
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words
```
