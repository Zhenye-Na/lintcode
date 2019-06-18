# 784. The Longest Common Prefix II

**Description**

Given `n` strings `dic` and a `target` string, output the maximum length of the longest common prefix of the target string with the given `n` strings.

The sum of the length of `n` strings is `sum`, `1 <= sum <= 50000`. The length of each string is greater than `0` (i.e. there is no empty string).

**Example**

Example 1

```
Input: dic = ["abcba","acc","abwsf"] and target = "abse"
Output: 2
Explanation:
The longest common prefix of “abse” and “abcba” is “ab”, and the length is 2. The longest common prefix of “abse” and “acc” is “a”, and the length is 1. The longest common prefix of “abse” and “abwsf” is “ab”, and the length is 2. max(2,1,2) = 2.
```

Example 2

```
Input: dic = ["aaa","bbb","aabb"] and target = "aaab"
Output: 3
Explanation:
The longest common prefix of “aaab” and “aaa” is “aaa”, and the length is 3. The longest common prefix of “aaab” and "bbb" is "", and the length is 0. The longest common prefix of “aaab” and “aabb” is “aa”, and the length is 2. max(3,0,2) = 3.
```


```python
class Solution:
    """
    @param words: the n strings
    @param target: the target string
    @return: The ans
    """
    def the_longest_common_prefix(self, words, target):
        # write your code here
        ans = 0
        for word in words:
            same = 0

            for j in range(0, len(target)):
                if j > len(word) - 1 or target[j] != word[j]:
                    break
                same += 1

            ans = max(ans, same)

        return ans
```