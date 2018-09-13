# 627. Longest Palindrome

Description
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Assume the length of given string will not exceed 1010.

Have you met this question in a real interview?  
Example
Given s = "abccccdd" return 7

One longest palindrome that can be built is "dccaccd", whose length is 7.

```
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        if s is None:
            return 0

        mapping = {}
        for i in xrange(len(s)):
            mapping[s[i]] = mapping.get(s[i], 0) + 1

        even, odd = 0, 0
        for k, v in mapping.iteritems():
            if v % 2 == 0:
                even += v
            if v % 2 == 1:
                odd = max(odd, v)

        return even + odd
```
