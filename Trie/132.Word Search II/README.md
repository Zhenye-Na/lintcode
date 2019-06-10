# 132. Word Search II

**Description**

Given a `matrix` of lower alphabets and a `dictionary`. Find all words in the `dictionary` that can be found in the `matrix`. A word can *start from any position* in the matrix and go `left/right/up/down` to the adjacent position. One character only be used once in one word. No same word in dictionary


**Example**

Example 1:

```
Input: ["doaf","agai","dcan"]，["dog","dad","dgdg","can","again"]
Output: ["again","can","dad","dog"]
Explanation:
  d o a f
  a g a i
  d c a n
search in Matrix，so return ["again","can","dad","dog"].
```


Example 2:

Input: ["a"], ["b"]
Output: []
Explanation:
 a
search in Matrix，return [].

**Challenge**

Using `trie` to implement your algorithm.


**Trie + DFS**


```python
class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_word = True
        node.word = word

    def find(self, word):
        node = self.root
        for ch in node.children:
            node = node.children.get(ch)
            if node is None:
                return None

        return node

    def searchWord(self, word):
        node = self.find(word)
        return node is not None and node.is_word

    def searchPrefix(self, prefix):
        node = self.find(prefix)
        return node is not None


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def wordSearchII(self, board, words):
        # write your code here
        if not board or not words or len(board) == 0 or len(words) == 0:
            return []

        trie = Trie()
        for word in words:
            trie.add(word)

        results = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                ch = board[i][j]
                self.dfs(board, trie.root.children.get(ch), i, j, set([(i, j)]), results, ch)

        results = list(results)
        return results

    def dfs(self, board, node, i, j, visited, results, current):
        if node is None:
            return

        if node.is_word:
            results.add(node.word)

        for k in range(4):
            x, y = i + self.dx[k], j + self.dy[k]
            if self._isValid(x, y, board, visited):
                ch = board[x][y]
                visited.add((x, y))
                self.dfs(board, node.children.get(ch), x, y, visited, results, current + ch)
                visited.remove((x, y))

    def _isValid(self, x, y, board, visited):
        return 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in visited
```

