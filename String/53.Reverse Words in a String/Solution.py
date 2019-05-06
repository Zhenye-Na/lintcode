class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        if not s or len(s) <= 1:
            return s

        s = s.strip()
        s_list = s.split(" ")

        for i in range(len(s_list)):
            s_list[i] = s_list[i].strip()
            s_list[i] = s_list[i][::-1]

        s_list = filter(None, s_list)
        s_prime = " ".join(s_list)[::-1]

        return s_prime