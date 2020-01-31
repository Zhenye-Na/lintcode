# 473. Add and Search Word - Data structure design

**Description**

Design a data structure that supports the following two operations: `addWord(word)` and `search(word)`

`search(word)` can search a *literal word* or a r*egular expression string* containing only letters `a-z` or `.` (period symbol).

```
A `.` means it can represent any one letter.
You may assume that all words are consist of lowercase letters `a-z`.
```

**Example**

Example 1:

```
Input:
  addWord("a")
  search(".")
Output:
  true
```

Example 2:

```
Input:
  addWord("bad")
  addWord("dad")
  addWord("mad")
  search("pad")  
  search("bad")  
  search(".ad")  
  search("b..")  
Output:
  false
  true
  true
  true
```


**Trie**

最开始的想法是: 如果当前字符是 `.`, 那么可以 iterate 一个 alphabet (26 个字母), recursively call self.search()

之后看了答案, 觉得确实根本不要在其他的节点上浪费时间, 直接在 children 节点里面遍历, 然后进行查找之后字符串

given `bad, dad, mad` -> search `..d`

就相当于, 第一次遍历 `b, d, m`, 然后在节点下面的 children 里面寻找是否有 `a`


```python
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """

    def addWord(self, word):
        # write your code here
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """

    def search(self, word):
        # write your code here
        if word is None:
            return False
        return self.search_helper(self.root, 0, word)

    def search_helper(self, node, idx, word):
        if node is None:
            return False

        if idx >= len(word):
            return node.is_word

        char = word[idx]
        if char != '.':
            return self.search_helper(node.children.get(char), idx + 1, word)

        for child in node.children:
            if self.search_helper(node.children[child], idx + 1, word):
                return True

        return False
```