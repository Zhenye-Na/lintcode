class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        dict = collections.Counter(A)
        for key in dict:
            if dict[key] == 1:
                return key
