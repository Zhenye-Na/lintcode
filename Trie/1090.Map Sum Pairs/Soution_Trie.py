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
