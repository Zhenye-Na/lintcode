class Solution:
    """
    @param string: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, string, left, right):
        # write your code here
        if not string or len(string) == 0:
            return string

        left, right = left % len(string), right % len(string)
        offset = 0
        if left >= right:
            offset = left - right
        else:
            offset = len(string) - (right - left)

        prefix = string[:offset][::-1]
        postfix = string[offset:][::-1]
        newString = prefix + postfix
        return newString[::-1]
