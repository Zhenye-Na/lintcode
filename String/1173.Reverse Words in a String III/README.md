# 1173. Reverse Words in a String III

**Description**

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

In the string, each word is separated by single space and there will not be any extra space in the string.


**Example**

```
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```

一行代码解决

```python
class Solution:
    """
    @param s: a string
    @return: reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order
    """
    def reverseWords(self, s):
        # Write your code here
        return " ".join([word[::-1] for word in s.strip().split()])
```