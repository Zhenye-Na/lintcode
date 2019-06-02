class Solution:
    """
    @param s: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, s):
        # Write your code here
        mapping = {}

        if not s or len(s) <= 0:
            return '0'

        for idx, char in enumerate(s):
            mapping[char] = mapping.get(char, 0) + 1

        for idx, key in enumerate(s):
            if mapping[key] == 1:
                return s[idx]

        return '0'
