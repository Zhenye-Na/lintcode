from collections import defaultdict
from collections import deque


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj_list, record = self.get_adj_record(equations, values)
        ans = []
        for q in queries:
            start, end = q[0], q[1]
            if start == end and start in adj_list:
                ans.append(1.0)
                continue
            queue, res, visited = deque(), -1.0, set()
            queue.append((start, 1.0))
            while queue and res == -1:
                cur_node, cur_val = queue.popleft()
                visited.add(cur_node)
                for nb in adj_list[cur_node]:
                    if nb in visited:
                        continue
                    new_val = cur_val * record[(cur_node, nb)]
                    if nb == end:
                        res = new_val

                        # 时间优化，这一步不一定需要
                        adj_list[start].add(nb)
                        adj_list[nb].add(start)
                        record[(start, nb)] = res
                        record[(nb, start)] = 1 / res

                        break
                    queue.append((nb, new_val))
            ans.append(res)
        return ans

    def get_adj_record(self, equations, values):
        adj_list, record = defaultdict(set), defaultdict(float)
        for i in range(len(equations)):
            u, v = equations[i][0], equations[i][1]
            adj_list[u].add(v)
            adj_list[v].add(u)
            record[(u, v)] = values[i]
            record[(v, u)] = 1 / values[i]
        return adj_list, record
