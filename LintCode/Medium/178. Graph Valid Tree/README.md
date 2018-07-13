# 178. Graph Valid Tree

- **Description**
    - Given n nodes labeled from `0` to `n - 1` and a list of **undirected edges** (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
    - You can assume that no duplicate edges will appear in edges. Since all edges are undirected, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in edges.
- **Example**
    - Given `n = 5` and edges = `[[0, 1], [0, 2], [0, 3], [1, 4]]`, return `true`.
    - Given `n = 5` and edges = `[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]`, return `false`.


## Solution

判断图是否可以看做成树。

- 如果一个树有 `n` 个 `nodes`，那么一定有 `n - 1` 个边
- 其次，从任意一个 `node` 开始，可以遍历整个图（树）
- 需要用一个 HashSet 来记录当前节点是否已经进入过 queue，以为题目明确指出 `undirected edges`，所以节点可能会重复出现


### Code

```java
public class Solution {
    /**
     * @param n: An integer
     * @param edges: a list of undirected edges
     * @return: true if it's a valid tree, or false
     */
    public boolean validTree(int n, int[][] edges) {
        // write your code here
        if (n == 0 || edges.length != n - 1) {
            return false;
        }

        // Collect neighbors
        Map<Integer, Set<Integer>> graph = initializeGraph(n, edges);

        // BFS
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> history = new HashSet<>();

        // labeled from 0 to n - 1
        queue.offer(0);
        history.add(0);
        int num = 0;

        while (!queue.isEmpty()) {

            int node = queue.poll();
            num++;

            for (Integer neighbor : graph.get(node)) {
                if (!history.contains(neighbor)) {
                    history.add(neighbor);
                    queue.offer(neighbor);
                }
            }
       }
       return (num == n);
    }

    private Map<Integer, Set<Integer>> initializeGraph(int n, int[][]edges) {
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        // Initialization
        for (int i = 0; i < n; i++) {
            graph.put(i, new HashSet<Integer>());
        }
        
        // Add neighbors
        for (int[] pair : edges) {
            int node1 = pair[0];
            int node2 = pair[1];
            graph.get(node1).add(node2);
            graph.get(node2).add(node1);
        }

        return graph;
    }

}
```
