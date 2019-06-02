class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        if divisor == 1:
            return self.isValid(dividend)

        if dividend == 0:
            return 0

        flag = 1 if dividend * divisor > 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)


        start, end = 0, dividend
        while start + 1 < end:
            mid = (end - start) / 2 + start

            if mid * divisor == dividend:
                return self.isValid(mid) * flag
            elif mid * divisor > dividend:
                end = mid
            elif mid * divisor < dividend:
                start = mid

        if end * divisor <= dividend:
            return self.isValid(end) * flag

        if start * divisor <= dividend:
            return self.isValid(start) * flag


    def isValid(self, num):
        INT_MAX = 2147483647
        return num if num <= INT_MAX  else INT_MAX
