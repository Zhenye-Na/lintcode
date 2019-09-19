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
