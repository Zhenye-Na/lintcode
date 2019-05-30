class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        if not chars or len(chars) == 0:
            return

        lo, hi = 0, len(chars) - 1
        while lo <= hi:
            while lo <= hi and chars[lo].islower():
                lo += 1
            while lo <= hi and chars[hi].isupper():
                hi -= 1
            if lo <= hi:
                chars[lo], chars[hi] = chars[hi], chars[lo]
                lo += 1
                hi -= 1
