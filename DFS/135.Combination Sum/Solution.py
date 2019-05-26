class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates or len(candidates) == 0:
            return [[]]

        candidates.sort()
        self.results = []
        self.target = target
        visited = [False for _ in range(len(candidates))]
        self._find_combination_sum(candidates, [], visited, 0)
        return self.results

    def _find_combination_sum(self, candidates, current_combination, visited, start):
        if sum(current_combination) == self.target:
            current_combination.sort()
            self.results.append(current_combination[:])
            return

        for i in range(start, len(candidates)):
            if sum(current_combination) + candidates[i] > self.target:
                break

            if i > 0 and candidates[i - 1] == candidates[i] and not visited[i - 1]:
                continue

            current_combination.append(candidates[i])
            visited[i] = True
            self._find_combination_sum(candidates, current_combination, visited, i)
            current_combination.pop()
            visited[i] = False