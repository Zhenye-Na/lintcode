# 1169. Permutation in String

**Description**

Given two strings `s1` and `s2`, write a function to return `true` if `s2` contains the permutation of `s1`. In other words, one of the first string's permutations is the substring of the second string.

```
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
```

**Example**

Example 1:

```
Input:s1 = "ab" s2 = "eidbaooo"
Output:true
Explanation: s2 contains one permutation of s1 ("ba").
```

Example 2:

```
Input:s1= "ab" s2 = "eidboaoo"
Output: false
```


**Two Pointers**

```python
class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def checkInclusion(self, s1, s2):
        # write your code here
        target = s1 
        source = s2 

        if len(target) > len(source):
            return False 

        target_hash = {} 
        source_hash = {}

        for i in range(len(target)):
            target_hash[target[i]] = target_hash.get(target[i], 0) + 1 
            source_hash[source[i]] = source_hash.get(source[i], 0) + 1 
            
        if target_hash == source_hash:
            return True 
            
        for window_start in range(1, len(source) - len(target) + 1):
            window_end = window_start + len(target) - 1 
            
            source_hash[source[window_end]] = source_hash.get(source[window_end], 0) + 1 
            source_hash[source[window_start - 1]] -= 1 

            if source_hash[source[window_start - 1]] == 0:
                del source_hash[source[window_start - 1]]

            if source_hash == target_hash:
                return True 

        return False
```


**DFS (TLE)**

写个 DFS - Permutations 练练手

```python
class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def checkInclusion(self, s1, s2):
        # write your code here
        if not s1 or not s2 or len(s1) > len(s2):
            return False

        sl = [ch for ch in s1]
        permutations = self.getPermutations(sl)
        for permutation in permutations:
            if s2.find(permutation) != -1:
                return True

        return False

    def getPermutations(self, sl):
        permutations = []
        visited = [False for _ in range(len(sl))]
        self.dfs(sl, permutations, [], visited)
        return permutations

    def dfs(self, sl, permutations, current, visited):
        if len(sl) == len(current):
            permutations.append("".join(current[:]))
            return

        for i in range(len(sl)):
            if not visited[i]:
                if i > 0 and sl[i - 1] == sl[i] and visited[i - 1]:
                    continue

                current.append(sl[i])
                visited[i] = True
                self.dfs(sl, permutations, current, visited)
                visited[i] = False
                current.pop()
```
