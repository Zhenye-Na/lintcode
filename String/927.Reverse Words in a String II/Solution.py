class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseWords(self, s):
        # write your code here
        if not s or len(s) <= 1:
            return s

        s_list = s.strip().split()
        s_list = list(filter(None, s_list))
        new_s = " ".join(reversed(s_list))

        return new_s

    def reverseWordsSolution2(self, s):
        return " ".join(reversed(s.strip().split(" ")))
