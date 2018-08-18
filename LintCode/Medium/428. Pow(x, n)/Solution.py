class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        if (x == 0):
            return 0

        if (n == 0):
            return 1

        if (n == 1):
            return x

        if n < 0:
            x = 1 / x
            n = - n

        tmp = self.myPow(x, n / 2)
        
        if (n % 2 == 0):
            return tmp * tmp
        else:
            return x * tmp * tmp