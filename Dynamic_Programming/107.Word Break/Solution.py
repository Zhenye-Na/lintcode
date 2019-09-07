class Solution:
    """
    @param: s: A string
    @param: dictionary: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dictionary):
        # write your code here
        if len(dictionary) == 0:
            return len(s) == 0

        # initialization
        # f[i] represents first i characters can be split, s[:i] in dictionary
        n = len(s)
        f = [False for _ in range(n + 1)]
        f[0] = True

        # function: f[i] <- f[j] with contraints
        max_len = max([len(word) for word in dictionary])
        for i in range(1, n + 1):
            for j in range(1, min(i, max_len) + 1):
                if not f[i - j]:
                    continue
                if s[i - j:i] in dictionary:
                    f[i] = True
                    break

        # answer: f[-1]
        return f[n]
