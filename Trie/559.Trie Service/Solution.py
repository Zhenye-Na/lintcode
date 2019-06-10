"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
        self.top10 = []
"""
class TrieService:

    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        # Return root of trie root, and 
        # lintcode will print the tree struct.
        return self.root

    # @param {str} word a string
    # @param {int} frequency an integer
    # @return nothing
    def insert(self, word, frequency):
        # Write your your code here
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

            node.top10.append(frequency)
            index = len(node.top10) - 1

            while index > 0:
                if node.top10[index] > node.top10[index - 1]:
                    node.top10[index], node.top10[index - 1] = node.top10[index - 1], node.top10[index]
                    index -= 1
                else:
                    break

            if len(node.top10) > 10:
                node.top10.pop()
