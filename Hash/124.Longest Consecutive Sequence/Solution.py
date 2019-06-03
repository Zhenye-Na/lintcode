class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        max_len = 0
        if not num or len(num) == 0:
            return max_len

        mapping = {number:True for number in num}
        for i in range(len(num)):
            if num[i] - 1 not in mapping:
                left, right = num[i], num[i] + 1
                while right in mapping:
                    right += 1
                max_len = max(max_len, right - left)

        return max_len
