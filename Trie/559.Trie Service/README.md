# 559. Trie Service

**Description**

Build tries from a list of `<word, freq>` pairs. Save top `10` for each node.

**Example**

Example 1

```
Input:  
 <"abc", 2>
 <"ac", 4>
 <"ab", 9>
Output:<a[9,4,2]<b[9,2]<c[2]<>>c[4]<>>> 
Explanation:
			Root
             / 
           a(9,4,2)
          /    \
        b(9,2) c(4)
       /
     c(2)
```

Example2

```
Input:  
<"a", 10>
<"c", 41>
<"b", 50>
<"abc", 5>
Output: <a[10,5]<b[5]<c[5]<>>>b[50]<>c[41]<>>
```

**Trie**

打擂台, 保存前 10 个

```python
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
```