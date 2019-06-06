class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        if not source or len(source) == 0:
            return ""

        if not target or len(target) == 0:
            return ""

        countS = [0 for _ in range(256)]
        countT = [0 for _ in range(256)]

        s = [_s for _s in source]
        t = [_t for _t in target]

        k = len(set(list(t)))
        for _t in t:
            countT[ord(_t)] += 1

        c, right = 0, 0
        l, r = -1, -1
        for left in range(len(s)):
            while right < len(s) and c < k:
                countS[ord(s[right])] += 1
                if countS[ord(s[right])] == countT[ord(s[right])]:
                    c += 1

                right += 1

            if c == k:
                if l == -1 or r - l > right - left:
                    l, r = left, right

            countS[ord(s[left])] -= 1
            if countS[ord(s[left])] == countT[ord(s[left])] - 1:
                c -= 1

        return "".join(s[l:r]) if l != -1 else ""
