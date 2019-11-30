class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return ""

        return self.dfs(s)

    def dfs(self, s):
        res = ""
        i = 0

        while i < len(s):
            if not s[i].isdigit():
                res += s[i]
                i += 1
                continue
            digit = ""

            while i < len(s) and s[i].isdigit():
                digit += s[i]
                i += 1
            left, right = i, i + 1
            left_p, right_p = 1, 0

            while right < len(s) and left_p != right_p:
                if s[right] == "[":
                    left_p += 1
                if s[right] == "]":
                    right_p += 1
                right += 1

            res += int(digit) * self.dfs(s[left + 1:right - 1])
            i = right

        return res
