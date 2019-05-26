# 1031. Is Graph Bipartite?

**Description**

Given an undirected graph, return `true` if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: `graph[i]` is a list of indexes `j` for which the edge between nodes i and j exists. Each node is an integer between `0` and `graph.length - 1`.

There are no self edges or parallel edges: `graph[i]` does not contain i, and it doesn't contain any element twice.


> 1. `graph` will have length in range `[1, 100]`.
> 2. `graph[i]` will contain integers in range `[0, graph.length - 1]`.
> 3. `graph[i]` will not contain `i` or duplicate values.
> 4. The graph is undirected: if any element `j` is in `graph[i]`, then `i` will be in `graph[j]`.

**Example**

Example 1:

```
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
  The graph looks like this:
  0----1
  |    |
  |    |
  3----2
  We can divide the vertices into two groups: {0, 2} and {1, 3}.
```

Example 2:

```
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
  The graph looks like this:
  0----1
  | \  |
  |  \ |
  3----2
  We cannot find a way to divide the set of nodes into two independent subsets.
```


**二分图染色模板题**

通过黑白染色我们可以判断一个无向图是否二分图:

遍历整个图, 将相邻的节点染成不同的颜色, 如果可以完成这个遍历(即染色过程没有冲突), 说明是二分图.

可以用 BFS 或 DFS 来实现, 只需要根据当前节点的颜色设定下一个节点的颜色即可, 如果下一个节点已经被染成了相同的颜色, 说明发生了冲突.

*DFS*

```python
class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    def isBipartite(self, graph):
        # Write your code here
        if not graph or len(graph) == 0:
            return False

        n = len(graph)
        self.colors = [0 for _ in range(n)]

        for i in range(n):
            if self.colors[i] == 0 and not self._colorize(i, 1, graph):
                return False

        return True


    def _colorize(self, current, color, graph):
        if self.colors[current] != 0:
            return self.colors[current] == color

        self.colors[current] = color
        for neighbor in graph[current]:
            if not self._colorize(neighbor, - color, graph):
                return False
        return True
```

*BFS*

```python
from collections import deque


class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    def isBipartite(self, graph):
        # Write your code here
        if not graph or len(graph) == 0:
            return False

        n = len(graph)
        visited = [0 for _ in range(n)]
        color = [0 for _ in range(n)]


        for i in range(n):
            if len(graph[i]) > 0 and visited[i] == 0:
                visited[i] = 1
                color[i] = 1
                queue = deque([i])

                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if visited[neighbor]:
                            if color[node] == color[neighbor]:
                                return False
                        else:
                            visited[neighbor] = 1
                            color[neighbor] = - color[node]
                            queue.append(neighbor)

        return True
```