import string
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        s = s.lower()
        translator = str.maketrans("", "", string.punctuation + " ")
        s = s.translate(translator)
        s = "".join(s.split(" "))
        return s == s[::-1]