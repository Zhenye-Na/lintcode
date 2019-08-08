# 582. Word Break II

**Description**

Given a string `s` and a dictionary of words `dict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

**Example**

Example 1:

```
Input: "lintcode", ["de","ding","co","code","lint"]
Output: ["lint code", "lint co de"]
Explanation:
insert a space is "lint code", insert two spaces is "lint co de".
```

Example 2:

```
Input: "a", []
Output: []
Explanation: dict is null.
```

**DFS**

```python
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        history = {}
        return self.dfs(s, wordDict, history)

    def dfs(self, s, wordDict, history):
        if s in history:
            return history[s]

        if len(s) == 0:
            return []

        res = []
        if s in wordDict:
            res.append(s)

        for i in range(1, len(s)):
            s1 = s[:i]
            s2 = s[i:]

            if s1 in wordDict:
                s2_res = self.dfs(s2, wordDict, history)
                for option in s2_res:
                    if option == '':
                        res.append(s1)
                    else:
                        res.append(s1 + ' ' + option)

        history[s] = res
        return res
```
