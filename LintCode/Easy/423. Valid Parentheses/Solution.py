class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False

        stack = []
        for symbol in s:
            if symbol == '(' or symbol == '[' or symbol == '{':
                stack.append(symbol)
            else:
                if not stack:
                    return False

                if (symbol == ')' and stack[-1] != '(') or (symbol == '}' and stack[-1] != '{') or (symbol == ']' and stack[-1] != '['):
                    return False

                stack.pop()

        return not stack
