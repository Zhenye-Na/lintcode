class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """

    def kDistinctCharacters(self, s, k):
        # Write your code here
        res = 0
        if not s or len(s) < k:
            return res

        for left in range(len(s)):
            right = left
            counter = set([])
            while right < len(s) and len(counter) < k:
                counter.add(s[right])
                right += 1

            if len(counter) == k:
                res += len(s) - right + 1

        return res
