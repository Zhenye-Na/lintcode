class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs or len(strs) == 0:
            return ""

        prefix = strs[0]
        i, j = 0, 0
        for word in strs[1:]:
            i, j = 0, 0
            while i < len(prefix) and j < len(word) and prefix[i] == word[j]:
                i += 1
                j += 1

            if j == 0:
                return ""
            elif 0 < j < len(word):
                prefix = prefix[:j]
            else:
                prefix = word

        return prefix
