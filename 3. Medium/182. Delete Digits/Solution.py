class Solution:
    """
    @param A: A positive integer which has N digits, A is a string
    @param k: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write your code here
        A = list(A)
        while k > 0:
            f = True
            for i in xrange(len(A)-1):
                if A[i] > A[i+1]:
                    del A[i]
                    f = False
                    break
            if f and len(A)>1:
                A.pop()
            k -= 1
        while len(A) > 1 and A[0]=='0':
            del A[0]
        return ''.join(A)
