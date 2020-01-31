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
