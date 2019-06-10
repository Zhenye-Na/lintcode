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
        for ch in word:
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
