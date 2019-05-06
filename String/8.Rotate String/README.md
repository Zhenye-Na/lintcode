# 8. Rotate String

**Description**

Given a string(Given in the way of char array) and an offset, rotate the string by offset in place. (rotate from left to right)


> `offset >= 0`  
> the length of str `>= 0`

**Example**

Example 1:

```
Input: str="abcdefg", offset = 3
Output: str = "efgabcd"	
Explanation: Note that it is rotated in place, that is, after str is rotated, it becomes "efgabcd".
```

Example 2:

```
Input: str="abcdefg", offset = 0
Output: str = "abcdefg"	
Explanation: Note that it is rotated in place, that is, after str is rotated, it becomes "abcdefg".
```

Example 3:

```
Input: str="abcdefg", offset = 1
Output: str = "gabcdef"	
Explanation: Note that it is rotated in place, that is, after str is rotated, it becomes "gabcdef".
```

Example 4:

```
Input: str="abcdefg", offset =2
Output: str = "fgabcde"	
Explanation: Note that it is rotated in place, that is, after str is rotated, it becomes "fgabcde".
```

Example 5:

```
Input: str="abcdefg", offset = 10
Output: str = "efgabcd"	
Explanation: Note that it is rotated in place, that is, after str is rotated, it becomes "efgabcd".
```

**Challenge**

Rotate in-place with O(1) extra memory.


```python
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if not s or len(s) == 0:
            return s

        offset = offset % len(s)
        start_index = len(s) - offset

        first, last = 0, start_index - 1
        while first + 1 <= last:
            tmp = s[first]
            s[first] = s[last]
            s[last] = tmp

            first += 1
            last -= 1

        last = len(s) - 1
        while start_index + 1 <= last:
            tmp = s[start_index]
            s[start_index] = s[last]
            s[last] = tmp

            start_index += 1
            last -= 1


        first, last = 0, len(s) - 1
        while first + 1 <= last:
            tmp = s[first]
            s[first] = s[last]
            s[last] = tmp

            first += 1
            last -= 1
```