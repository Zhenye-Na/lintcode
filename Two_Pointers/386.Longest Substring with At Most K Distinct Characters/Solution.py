class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s or len(s) == 0:
            return 0

        chars = [_s for _s in s]
        c = 0

        visited = [0 for _ in range(256)]
        left, right = 0, 0
        l, r = -1, -1
        for left in range(len(chars)):
            while right < len(chars) and c <= k:
                if visited[ord(chars[right])] == 0:
                    c += 1

                if c > k:
                    c -= 1
                    break

                visited[ord(chars[right])] += 1
                right += 1

            if c <= k:
                if l == -1 or r - l < right - left:
                    l, r = left, right

            visited[ord(chars[left])] -= 1
            if visited[ord(chars[left])] == 0:
                c -= 1

        return r - l
