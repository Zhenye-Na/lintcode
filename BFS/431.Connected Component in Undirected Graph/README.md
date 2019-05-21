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


**Union Find**

Find parent用来寻根，中间遍历建立关系，同时union，结果输出略加处理。（我感觉set输出就可以了）

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
