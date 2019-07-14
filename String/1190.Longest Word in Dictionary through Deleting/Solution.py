class Solution:
    """
    @param s: a string
    @param d: List[str]
    @return: return a string
    """

    def findLongestWord(self, s, d):
        # write your code  here
        for x in sorted(d, key=lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in x):
                return x
        return ''
