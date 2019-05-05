class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if not s or len(s) == 0:
            return s

        offset = offset % len(s)
        start_index = len(s) - offset

        first, last = 0, start_index - 1
        while first + 1 <= last:
            tmp = s[first]
            s[first] = s[last]
            s[last] = tmp

            first += 1
            last -= 1

        last = len(s) - 1
        while start_index + 1 <= last:
            tmp = s[start_index]
            s[start_index] = s[last]
            s[last] = tmp

            start_index += 1
            last -= 1


        first, last = 0, len(s) - 1
        while first + 1 <= last:
            tmp = s[first]
            s[first] = s[last]
            s[last] = tmp

            first += 1
            last -= 1
