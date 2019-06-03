from collections import defaultdict


class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        result = []
        if not strs or len(strs) == 0:
            return result

        mapping = defaultdict(list)
        for word in strs:
            word_set = "".join(sorted(word))
            mapping[word_set].append(word)

        for key in mapping:
            if len(mapping[key]) >= 2:
                result += mapping[key]

        return result
