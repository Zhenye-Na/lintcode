# 1088. Redundant Connection

**Description**

In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values `1, 2, ..., N`), with one additional edge added. The added edge has two different vertices chosen from `1` to `N`, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair `[u, v]` with `u < v`, that represents an undirected edge connecting nodes `u` and `v`.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge `[u, v]` should be in the same format, with `u < v`.

```
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
```

**Example**

Example 1:

```
Input:  [[1,2], [1,3], [2,3]]
Output:  [2,3]	
Explanation: 
  looks like:
	  1
	 / \
	2 - 3
```

Example 2:

```
Input:  [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output:  [1,4]	
Explanation:
	looks like:
	5 - 1 - 2
	    |   |
	    4 - 3
```

**Union Find**

```python
class UnionFind:

    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}

    def find(self, node):
        path = []
        while node != self.parent[node]:
            path.append(node)
            node = self.parent[node]

        for p in path:
            self.parent[p] = node

        return node

    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 != parent2:
            self.parent[max(parent1, parent2)] = min(parent1, parent2)
            return False

        return True


class Solution:
    """
    @param edges: List[List[int]]
    @return: List[int]
    """

    def findRedundantConnection(self, edges):
        # write your code here
        if not edges or len(edges) == 0:
            return [0, 0]

        ans = []
        max_node = -1
        for edge in edges:
            max_node = max(max_node, max(edge))

        uf = UnionFind(max_node)
        for edge in edges:
            res = uf.union(edge[0], edge[1])
            if res:
                ans.append(edge)

        return ans.pop() if ans else [0, 0]
```
