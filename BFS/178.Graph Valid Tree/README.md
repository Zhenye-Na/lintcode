# 178. Graph Valid Tree

**Description**

Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in edges.

**Example**

Example 1:

```
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
```

Example 2:

```
Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
```

**BFS**

1. `n` 个节点的图想要变成"树", 必须是两两连接, 边的个数为 `n - 1`
2. 通过 BFS 遍历 Graph, 可以遍历到所有节点, 不会遗漏

用到 python 特有的数据结构

- deque
- defauldict

```python
from collections import deque, defaultdict

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n <= 1:
            return True

        # Contraint 1: # of edges equals to # of node minus 1
        if len(edges) != n - 1:
            return False

        # map from integer -> set of neighbors
        mapping = self._get_neighbors(edges)

        # Constraint 2: # of onnected component in the graph is 1
        queue = deque([])
        queue.append(0)
        history = set()

        while queue:
            node = queue.popleft()
            for neighbor in mapping[node]:
                if neighbor not in history:
                    queue.append(neighbor)
                    history.add(neighbor)

        if len(history) == n:
            return True
        return False

    def _get_neighbors(self, edges):
        mapping = defaultdict(list)
        for edge in edges:
            source, target = edge
            mapping[source].append(target)
            mapping[target].append(source)

        return mapping
```

**Union Find**


```python
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if n - 1 != len(edges):
            return False

        self.father = {i: i for i in range(n)}
        self.size = n

        for a, b in edges:
            self.union(a, b)

        return self.size == 1

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.size -= 1
            self.father[root_a] = root_b

    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node
```
