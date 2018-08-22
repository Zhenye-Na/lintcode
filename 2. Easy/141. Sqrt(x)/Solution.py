class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if (x == 0): return x

        start, end = 1, x

        while (start + 1 < end):
            mid = (end - start) // 2 + start

            if (mid ** 2 == x):
                return mid
            elif (mid ** 2 > x):
                end = mid
            else:
                start = mid

        if (start ** 2 <= x):
            return start
        else:
            return end
