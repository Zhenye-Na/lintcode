class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def checkInclusion(self, s1, s2):
        # write your code here
        if not s1 or not s2 or len(s1) > len(s2):
            return False

        sl = [ch for ch in s1]
        permutations = self.getPermutations(sl)
        for permutation in permutations:
            if s2.find(permutation) != -1:
                return True

        return False

    def getPermutations(self, sl):
        permutations = []
        visited = [False for _ in range(len(sl))]
        self.dfs(sl, permutations, [], visited)
        return permutations

    def dfs(self, sl, permutations, current, visited):
        if len(sl) == len(current):
            permutations.append("".join(current[:]))
            return

        for i in range(len(sl)):
            if not visited[i]:
                if i > 0 and sl[i - 1] == sl[i] and visited[i - 1]:
                    continue

                current.append(sl[i])
                visited[i] = True
                self.dfs(sl, permutations, current, visited)
                visited[i] = False
                current.pop()
