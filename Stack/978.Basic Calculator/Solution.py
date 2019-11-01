class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """

    def calculate(self, s):
        # Write your code here
        s = s.replace(" ", "")
        stack = []
        result = 0
        number = 0
        sign = 1

        for c in s:
            if c in '1234567890':
                number = number * 10 + int(c)
            elif c == '+':
                result += sign * number
                number = 0
                sign = 1
            elif c == '-':
                result += sign * number
                number = 0
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ')':
                result += sign * number
                number = 0
                result *= stack[-1]
                result += stack[-2]
                stack = stack[:-2]

        result += sign * number

        return result
