# 49. Sort Letters by Case

**Description**

Given a string which contains only letters. Sort it by **lower case first** and **upper case second**.

It's **NOT** necessary to keep the original order of lower-case letters and upper case letters.


**Example**

```
Example 1:
	Input:  "abAcD"
	Output:  "acbAD"

Example 2:
	Input: "ABC"
	Output:  "ABC"
```

**Challenge**

Do it in one-pass and in-place.

**Two Pointers**

```python
class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        if not chars or len(chars) == 0:
            return

        lo, hi = 0, len(chars) - 1
        while lo <= hi:
            while lo <= hi and chars[lo].islower():
                lo += 1
            while lo <= hi and chars[hi].isupper():
                hi -= 1
            if lo <= hi:
                chars[lo], chars[hi] = chars[hi], chars[lo]
                lo += 1
                hi -= 1
```