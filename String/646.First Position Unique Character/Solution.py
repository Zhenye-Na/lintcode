from collections import Counter


class Solution:
    """
    @param s: a string
    @return: it's index
    """

    def firstUniqChar(self, s):
        # write your code here
        counter = Counter(s)

        for idx, char in enumerate(s):
            if counter[char] == 1:
                return idx

        return -1
