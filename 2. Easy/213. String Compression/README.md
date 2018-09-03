# 213. String Compression

- **Description**
    - Implement a method to perform basic string compression using the counts of repeated characters. For example, the string `aabcccccaaa` would become `a2b1c5a3`.
    - **If the "compressed" string would not become smaller than the original string, your method should return the original string.**
    - You can assume the string has only upper and lower case letters (a-z).
- **Example**
    - `str = aabcccccaaa` return `a2b1c5a3`
    - `str = aabbcc` return `aabbcc`
    - `str = aaaa` return `a4`


## Solution

用一种很“无脑”的做法，过一遍即可

### Python

```python
class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        # write your code here
        if not originalString or len(originalString) == 1:
            return originalString

        mapping = {}
        mapping[originalString[0]] = 0
        result = ""

        for os in originalString:
            if os not in mapping:
                newSubString = mapping.keys()[0] + str(mapping.get(mapping.keys()[0]))
                result += newSubString
                mapping.clear()

            mapping[os] = mapping.get(os, 0) + 1

        newSubString = mapping.keys()[0] + str(mapping.get(mapping.keys()[0]))
        result += newSubString
        return result if len(result) < len(originalString) else originalString

```