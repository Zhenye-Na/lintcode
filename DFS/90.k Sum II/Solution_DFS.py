class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, A, k, target):
        # write your code here
        self.result = []
        if not A or len(A) == 0:
            return self.result

        if k > len(A) and sum(A) != target:
            return self.result

        self.dfs(A, k, [], 0, target)
        return self.result

    def dfs(self, A, k, curr, start, target):
        if len(curr) == k and target == 0:
            self.result.append(curr[:])
            return

        for idx in range(start, len(A)):
            if target >= A[idx]:
                curr.append(A[idx])
                self.dfs(A, k, curr, idx + 1, target - A[idx])
                curr.pop()
