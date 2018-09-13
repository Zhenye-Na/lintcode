class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        # write your code here
        if num / 10 == 0:
            return True

        numString = str(num)
        start, end = 0, len(numString) - 1
        while start < end:
            if numString[start] != numString[end]:
                return False
            start += 1
            end -= 1

        return True
