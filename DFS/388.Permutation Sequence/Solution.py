class Solution:
    """
    @param n: n
    @param k: the k th permutation
    @return: return the k-th permutation
    """
    def getPermutation(self, n, k):
        # write your code here
        nums = [str(i) for i in range(1, n + 1)]
        self.permutations = []
        self.dfs(nums, [])

        return self.permutations[k - 1]

    def dfs(self, nums, current):
        if len(current) == len(nums):
            self.permutations.append(''.join(current[:]))
            return

        for num in nums:
            if num not in current:
                current.append(num)
                self.dfs(nums, current)
                current.pop()
