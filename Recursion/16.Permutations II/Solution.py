class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return [[]]

        nums.sort()
        visited = [False for _ in range(len(nums))]
        permutations = []
        self._find_permutations(nums, permutations, [], visited)
        return permutations

    def _find_permutations(self, nums, permutations, tmp, visited):
        if len(tmp) == len(nums):
            permutations.append(tmp[:])
            return

        for i in range(len(nums)):
            if not visited[i]:
                # remove duplicates
                if i > 0 and nums[i - 1] == nums[i] and visited[i - 1]:
                    continue

                # backtracking
                visited[i] = True
                tmp.append(nums[i])
                self._find_permutations(nums, permutations, tmp, visited)
                tmp.pop()
                visited[i] = False
