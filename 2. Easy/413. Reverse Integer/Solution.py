class Solution:
    """
    @param x: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, x):
        # write your code here
        result = 0
        flag = 1 if x > 0 else -1
        x = abs(x)

        stack = []
        while x != 0:
            stack.append(x % 10)
            x /= 10

        while stack:
            result = (result * 10) + stack.pop(0)

        return result * flag if (result * flag) < 2 ** 31 - 1 and (result * flag) > -2 ** 31 else 0
