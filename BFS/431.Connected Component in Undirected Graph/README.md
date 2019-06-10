# 431. Connected Component in Undirected Graph

**Description**

Find connected component in undirected graph.

Each node in the graph contains a label and a list of its neighbors.

(A connected component of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

You need return a list of label set.

```
Nodes in a connected component should sort by label in ascending order. Different connected components can be in any order.
```

**Example**

Example 1:

```
Input: {1,2,4#2,1,4#3,5#4,1,2#5,3}
Output: [[1,2,4],[3,5]]
Explanation:

  1------2  3
   \     |  | 
    \    |  |
     \   |  |
      \  |  |
        4   5
```

Example 2:

```
Input: {1,2#2,1}
Output: [[1,2]]
Explanation:

  1--2
```

**BFS**

```python
from collections import deque

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param {UndirectedGraphNode[]} nodes an array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        connected_components = []

        if not nodes or len(nodes) == 0:
            return connected_components

        visited = set()

        for node in nodes:
            if node in visited:
                continue
            
            component = []
            queue = deque([node])
            visited.add(node)

            while queue:
                cur_node = queue.popleft()
                component.append(cur_node.label)
                for neighbor in cur_node.neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

            component.sort()
            connected_components.append(component)

        return connected_components

```

**Union Find 1**

初始化的时候建立一个 children 字典, 在 union 的时候, 如果合并了, 那么把 children 字典也合并, 最后输出 列表不为空的即可

```python
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
from collections import defaultdict

class UnionFind:
    def __init__(self, nodes):
        self.father = {}
        self.children = defaultdict(list)
        for node in nodes:
            self.father[node.label] = node.label
            self.children[node.label].append(node.label)

    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]
        for n in path:
            self.father[n] = node
        return node

    def union(self, nodeA, nodeB):
        rootA, rootB = self.find(nodeA), self.find(nodeB)
        if rootA != rootB:
            self.father[rootA] = rootB
            self.children[rootB].extend(self.children[rootA])
            self.children[rootA] = []


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        uf = UnionFind(nodes)

        for node in nodes:
            for neighbor in node.neighbors:
                uf.union(node.label, neighbor.label)

        result = []
        for k, v in uf.children.items():
            if len(v) > 0:
                result.append(sorted(v))

        return result
```


**Union Find 2**

Find parent用来寻根，中间遍历建立关系，同时union，结果输出略加处理。

```python
class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def __init__(self):
        self.d = {}

    def connectedSet(self, nodes):
        # write your code here
        for n in nodes:
            self.d[n.label] = None

        for node in nodes:
            for n in node.neighbors:
                a = self.find_parent(node.label)
                b = self.find_parent(n.label)
                if a != b:
                    self.d[a] = b

        result = {}
        for k in self.d:
            key = self.find_parent(k)
            result[key] = result.get(key, []) + [k]

        # Not sure why the result must be sorted to pass... Maybe set?
        return sorted([sorted(i) for i in result.values()])

    def find_parent(self, n):
        if self.d[n] is not None:
            return self.find_parent(self.d[n])
        return n
```
