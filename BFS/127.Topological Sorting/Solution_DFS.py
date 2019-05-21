def topSortDFS(self, graph):

        def dfs(indegree, g, ans):
            ans.append(g)
            indegree[g] = -1 

            for c in g.neighbors:
                indegree[c] -= 1
                if indegree[c] == 0:
                    dfs(indegree, c, ans)
                    
        indegree = {}
        ans = []

        for g in graph:
            for n in g.neighbors:
                if n not in indegree:
                    indegree[n] = 1
                else:
                    indegree[n] += 1

        for g in graph:
            if g not in indegree or indegree[g] == 0:
                dfs(indegree, g, ans)
        return ans
