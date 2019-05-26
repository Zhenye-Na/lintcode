class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        self.results = []

        if not num or len(num) == 0:
            return self.results

        num.sort()
        self.target = target
        self.visited = [False for _ in range(len(num))]

        self._find_combination_sum_unique(num, [], 0)
        return self.results

    def _find_combination_sum_unique(self, num, tmp, start):
        if sum(tmp) == self.target:
            tmp2 = sorted(tmp)
            self.results.append(tmp2)
            return

        for i in range(start, len(num)):
            if sum(tmp) + num[i] > self.target:
                break

            if not self.visited[i]:

                # remove duplicates
                if i > 0 and num[i - 1] == num[i] and not self.visited[i - 1]:
                    continue

                self.visited[i] = True
                tmp.append(num[i])
                self._find_combination_sum_unique(num, tmp, i + 1)
                tmp.pop()
                self.visited[i] = False
