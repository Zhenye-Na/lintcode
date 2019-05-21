# 127. Topological Sorting

**Description**

Given an directed graph, a topological order of the graph nodes is defined as follow:

```
For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.
```

You can assume that there is at least one topological order in the graph.


**Example**

For graph as follow:

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThE9AgZZszyhwe0o9qpp3VyizdIj9kWwMY50HiQEysXvkSLsoZ)

The topological order can be:

```
[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
```


**Challenge**

Can you do it in both BFS and DFS?


**Follow up**

如果图里面有环, 如果不存在拓扑排序, 返回 None

- 加上一句话就可以解决 `return order if len(order) == len(graph) else None`
- 因为如果有环, 最后肯定会出现还有没访问过的点, 但是那些点的入度都不是 `0`, 无法入 `queue`, 所以最后得到的结果中结点个数要比图小


**BFS**

给定一个有向图，图节点的拓扑排序被定义为：

- 对于每条有向边 `A -> B`, 则 `A` 必须排在 `B` 之前
- 拓扑排序的第一个节点可以是任何在图中没有其他节点指向它的节点


```python
from collections import deque

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if graph is None:
            return []

        order = []
        queue = deque([])
        indegree = self._getIndegree(graph)

        for node, nodeIndegree in indegree.items():
            if nodeIndegree == 0:
                queue.append(node)

        while queue:
            graphNode = queue.popleft()
            order.append(graphNode)

            for neighbor in graphNode.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)


        return order if len(order) == len(graph) else None


    def _getIndegree(self, graph):
        indegree = {x: 0 for x in graph}
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1

        return indegree
```