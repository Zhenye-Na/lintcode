class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        if not s or not t:
            return False

        n, m = len(s), len(t)
        if abs(n - m) == 0:
            return self.replaceOneChar(s, t)
        if abs(n - m) == 1:
            if n > m:
                return self.deleteOneChar(s, t)
            else:
                return self.deleteOneChar(t, s)

        return False

    def replaceOneChar(self, word1, word2):
        flag = False
        for i in range(len(word2)):
            if word1[i] != word2[i]:
                if flag:
                    return False
                else:
                    flag = True

        return flag


    def deleteOneChar(self, word1, word2):
        fast, slow = 0, 0
        flag = False
        while slow < len(word2):
            if word1[fast] != word2[slow]:
                if flag:
                    return False

                flag = True
                slow -= 1

            slow += 1
            fast += 1

        return True
