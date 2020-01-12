# 1110. Replace Words

**Description**

In English, we have a concept called `root`, which can be followed by some other words to form another longer word - let's call this word `successor`. For example, the root `an`, followed by `other`, which can form another word another.

Now, given a `dictionary` consisting of many `roots` and a `sentence`. You need to replace all the successor in the sentence with the root forming it. If a `successor` has many `roots` can form it, replace it with the root with the **shortest** length.

You need to output the sentence after the replacement.

```
The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
```

**Example**

Example 1:

```
Input: 
dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: 
"the cat was rat by the bat"
```

Example 2:

```
Input: 
dict = ["go", "begin", "make","end"]
sentence = "a good beginning makes a good ending"
Output: 
"a go begin make a go end"
```

**Trie**

```python
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_word = True
        node.word = word

    def _find(self, word):
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return None
            elif node.is_word == True:
                return node

    def searchRoot(self, word):
        node = self._find(word)
        if node is not None:
            return node.word
        else:
            return word


class Solution:
    """
    @param dictionary: List[str]
    @param sentence: a string
    @return: return a string
    """

    def replaceWords(self, dictionary, sentence):
        # write your code here
        replaced_sentence = []
        if dictionary is None or sentence is None or len(dictionary) == 0 or len(sentence) == 0:
            return replaced_sentence

        trie = Trie()
        for root_word in dictionary:
            trie.insert(root_word)

        sentence_list = sentence.split()

        for word in sentence_list:
            new_word = trie.searchRoot(word)
            replaced_sentence.append(new_word)

        return " ".join(replaced_sentence)
```
