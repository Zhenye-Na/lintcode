# 442. Implement Trie (Prefix Tree)

**Description**

Implement a Trie with insert, search, and startsWith methods.

You may assume that all inputs are consist of lowercase letters `a-z`.

**Example**

Example 1:

```
Input:
  insert("lintcode")
  search("lint")
  startsWith("lint")
Output:
  false
  true
```

Example 2:

```
Input:
  insert("lintcode")
  search("code")
  startsWith("lint")
  startsWith("linterror")
  insert("linterror")
  search("lintcode)
  startsWith("linterror")
Output:
  false
  true
  false
  true
  true
```

**Trie**

模板题

```python
class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()


    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_word = True


    """
    return the node in the trie if exists 
    """
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node


    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        node = self.find(word)
        return node is not None and node.is_word


    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        return self.find(prefix) is not None
```