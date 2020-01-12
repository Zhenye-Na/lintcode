# 1090. Map Sum Pairs

**Description**

Implement a `MapSum` class with `insert`, and `sum` methods.

For the method insert, you'll be given a pair of `(string, integer)`. The string represents the key and the integer represents the value. If the key already existed, then the original `key-value` pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the `sum` of all the pairs' value whose key starts with the prefix.

**Example**

```
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
```

**Trie**

```python
"""
Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert(key,val)
param_2 = obj.sum(prefix)
"""


class TrieNode:

    def __init__(self):
        self.children = {}
        self.val = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.mapping = {}

    def add(self, word, val):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.val += val

    def searchPrefix(self, prefix):
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return 0

        return node.val


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        self.d = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key in self.d:
            self.trie.add(key, val - self.d[key])
        else:
            self.trie.add(key, val)

        self.d[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.trie.searchPrefix(prefix)
```


**HashMap**

```python
class MapSum(object):
    def __init__(self):
        self.map = {}
        self.score = collections.Counter()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        for i in xrange(len(key) + 1):
            prefix = key[:i]
            self.score[prefix] += delta

    def sum(self, prefix):
        return self.score[prefix]
```