class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        # write your code here
        if not A or len(A) % 3 != 1:
            return -1

        bits = [0 for _ in range(32)]
        for a in A:
            for j in range(32):
                if ((1 << j) & a) > 0:
                    bits[j] += 1

        ans = 0
        for i in range(32):
            t = bits[i] % 3
            if t == 1:
                ans = ans + (1 << i)

        return ans