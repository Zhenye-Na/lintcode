# 415. Valid Palindrome

**Description**

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

**Example**

Example 1:

```
Input: "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama"
```

Example 2:

```
Input: "race a car"
Output: false
Explanation: "raceacar"
```

**Challenge**

`O(n)` time without extra memory.



```python
import string
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        s = s.lower()
        translator = str.maketrans("", "", string.punctuation + " ")
        s = s.translate(translator)
        s = "".join(s.split(" "))
        return s == s[::-1]
```
