class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []
        if not s or len(s) == 0:
            return s

        word = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                rep = 0
                while s[i].isdigit():
                    rep = rep * 10 + int(s[i])
                    i += 1
                stack.append(str(rep))

            elif s[i] == "[":
                i += 1
                continue

            elif s[i] == "]":
                while not stack[-1].isdigit():
                    word.append(stack.pop())

                s_prime = ""
                while word:
                    s_prime += word.pop()

                s_prime = int(stack[-1]) * s_prime
                stack.pop()
                stack.append(s_prime)

                i += 1

            else:
                stack.append(s[i])
                i += 1

        return "".join(stack)
