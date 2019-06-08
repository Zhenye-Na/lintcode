# 591. Connecting Graph III

**Description**

Given `n` nodes in a graph labeled from `1` to `n`. There is no edges in the graph at beginning.

You need to support the following method:

- `connect(a, b)`, an edge to connect node `a` and node `b`
- `query()`, Returns the number of connected component in the graph

**Example**

Example 1:

```
Input:
ConnectingGraph3(5)
query()
connect(1, 2)
query()
connect(2, 4)
query()
connect(1, 4)
query()

Output:[5,4,3,3]
```

Example 2:

```
Input:
ConnectingGraph3(6)
query()
query()
query()
query()
query()


Output:
[6,6,6,6,6]
```

**Union Find**

并查集。

实时维护区域的个数，即若在某一次合并中两个区域合并成一个，那么数量 `-1`。


```python
class ConnectingGraph3:

    def __init__(self, n):
        self.father = {}
        for i in range(1, n + 1):
            self.father[i] = i
        self.size = n

    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        root_a = self._find(a)
        root_b = self._find(b)
        if root_b != root_a:
            self.father[root_a] = root_b
            self.size -= 1

    def _find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node
    """
    @return: An integer
    """
    def query(self):
        # write your code here
        return self.size
```