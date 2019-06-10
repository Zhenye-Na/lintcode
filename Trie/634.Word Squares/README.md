# 634. Word Squares

**Description**

Given a set of words without duplicates, find all word squares you can build from them.

A sequence of words forms a valid word square if the `k`th row and column read the exact same string, where `0 <= k < max(numRows, numColumns)`.

For example, the word sequence `["ball","area","lead","lady"]` forms a word square because each word reads the same both horizontally and vertically.

```
b a l l
a r e a
l e a d
l a d y
```

- There are at least `1` and at most `1000` words.
- All words will have the exact *same* length.
- Word length is at least `1` and at most `5`.
- Each word contains only lowercase English alphabet `a-z`.


**Example**

Example 1:

```
Input:
["area","lead","wall","lady","ball"]

Output:
[["wall","area","lead","lady"],["ball","area","lead","lady"]]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
```

Example 2:

```
Input:
["abat","baba","atan","atal"]
Output:
[["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
```

**Trie + DFS + Pruning**

可行性剪枝

关键在于写出前缀, 并且把每个单词记录在每个节点上更容易判断

```python
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list = []


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for chidx, ch in enumerate(word):
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.word_list.append(word)

        node.is_word = True

    def find(self, word):
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def searchWord(self, word):
        node = self.find(word)
        return node is not None and node.is_word

    def searchPrefix(self, prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_list


class Solution:
    """
    @param: words: a list of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        # write your code here
        if not words or len(words) == 0:
            return []

        trie = Trie()
        for word in words:
            trie.add(word)

        results = []
        for word in words:
            self.dfs(trie, [word], results)

        return results


    def dfs(self, trie, word_square, results):
        idx, n = len(word_square), len(word_square[0])

        if idx == n:
            results.append(word_square[:])
            return

        # dfs pruning
        for row_index in range(idx, n):
            prefix = "".join([word_square[i][row_index] for i in range(idx)])
            if not trie.searchPrefix(prefix):
                return

        prefix = "".join([word_square[i][idx] for i in range(idx)])
        for word in trie.searchPrefix(prefix):
            word_square.append(word)
            self.dfs(trie, word_square, results)
            word_square.pop()
```