class Solution:
    """
    @param A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        # write your code here
        if A is None or len(A) % 2 != 0:
            return []

        xor = 0
        for num in A:
            xor ^= num

        diff = xor & (~ (xor - 1))
        res = [0] * 2
        for num in A:
            if num & diff == 0:
                res[0] ^= num
            else:
                res[1] ^= num

        return res
