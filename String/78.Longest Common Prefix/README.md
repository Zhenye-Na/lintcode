# 78. Longest Common Prefix

**Description**

Given `k` strings, find the longest common prefix (LCP).

**Example**

Example 1:

```
Input:  "ABCD", "ABEF", "ACEF"
Output:  "A"
```

Example 2:

```
Input: "ABCDEFG", "ABCEFG" and "ABCEFA"
Output:  "ABC"
```

枚举, 如果变成空, 那么就是没有直接 `return`

```python
class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs or len(strs) == 0:
            return ""

        prefix = strs[0]
        i, j = 0, 0
        for word in strs[1:]:
            i, j = 0, 0
            while i < len(prefix) and j < len(word) and prefix[i] == word[j]:
                i += 1
                j += 1

            if j == 0:
                return ""
            elif 0 < j < len(word):
                prefix = prefix[:j]
            else:
                prefix = word

        return prefix
```

**Trie**

如何判断 prefix 长度? 根据 `node.children` 字典的长度, 如果超过了 `1` 那么说明 `prefix` 已经到头啦, 返回结果

注意空串的 edge case

时间复杂度 遍历一次 `O(n)`, 插入 `O(k)` k 是单词长度 -> `O(nk)`

`find()` 函数没用到, 但是为了复习写了一下

```python
class TrieNode:

    def __init__(self):
        self.children = {}


class Trie:

    def __init__(self):
        
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

    def find(self, word):
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return None

        return node


class Solution:
    """
    @param words: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, words):
        # write your code here
        trie = Trie()
        for word in words:
            if not word or len(word) == 0:
                return ""
            trie.insert(word)

        node = trie.root
        res = ""
        while True:
            if len(node.children) == 1:
                res += list(node.children.keys())[0]
            else:
                break
            node = node.children[list(node.children.keys())[0]]

        return res
```