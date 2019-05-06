class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A or len(A) == 0:
            return None

        diff = [abs(e - target) for e in A]
        results = [a for _, a in sorted(zip(diff, A))]
        return results[:k]
