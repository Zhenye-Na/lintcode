class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def __init__(self):
        self.result = []
    
    def combine(self, n, k):
        # write your code here
        if n == 0 or k == 0:
            return self.result

        self.helper([], n, k, 1, k)
        return self.result


    def helper(self, combo, n, k, start, l):
        if len(combo) == l:
            self.result.append(combo[:])
            return
        
        for i in range(start, n+1):
            combo.append(i)
            self.helper(combo, n, k-1, i+1, l)
            combo.pop()