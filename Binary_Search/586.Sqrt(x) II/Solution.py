class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        if not x:
            return

        left, right = 0, max(1, x)
        while right - left > 1e-10:
            mid = left + (right - left) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid
            else:
                right = mid

        return left