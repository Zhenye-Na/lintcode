# 171. Anagrams

**Description**

Given an array of strings, return all groups of strings that are anagrams.

> All inputs will be in **lower-case**

**Example**

Example 1:

```
Input:["lint", "intl", "inlt", "code"]
Output:["lint", "inlt", "intl"]
```

Example 2:

```
Input:["ab", "ba", "cd", "dc", "e"]
Output: ["ab", "ba", "cd", "dc"]
```

**What is Anagram?**

Two strings are anagram if they can be the same after change the order of characters.

**HashMap**

```python
from collections import defaultdict


class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        result = []
        if not strs or len(strs) == 0:
            return result

        mapping = defaultdict(list)
        for word in strs:
            word_set = "".join(sorted(word))
            mapping[word_set].append(word)

        for key in mapping:
            if len(mapping[key]) >= 2:
                result += mapping[key]

        return result
```