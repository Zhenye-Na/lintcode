# 137. Clone Graph

**Description**

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.

You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

```
You need return the node with the same label as the input node.
```

**BFS**

使用宽度优先搜索 BFS 的版本

- 第一步: 找到所有的点  
- 第二步: 复制所有的点, 将映射关系存起来  
- 第三步: 找到所有的边, 复制每一条边


```python
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return None

        # get all the nodes in the graph
        nodes = self._get_nodes(node)

        # map from original node to new node
        mapping = dict()

        # copy ndoes
        for graphNode in nodes:
            mapping[graphNode] = UndirectedGraphNode(graphNode.label)

        # copy edges
        for graphNode in nodes:
            for neighbor in graphNode.neighbors:
                newNeighbor = mapping[neighbor]
                mapping[graphNode].neighbors.append(newNeighbor)

        return mapping[node]


    def _get_nodes(self, node):
        from collections import deque

        queue = deque([])
        history = set()
        nodes = []

        queue.append(node)
        history.add(node)

        while queue:
            graphNode = queue.popleft()
            nodes.append(graphNode)

            for neighbor in graphNode.neighbors:
                if neighbor not in history:
                    queue.append(neighbor)
                    history.add(neighbor)

        return nodes
```