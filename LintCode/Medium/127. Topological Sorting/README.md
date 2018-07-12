# 127. Topological Sorting


- **Description**
    - Given an directed graph, a topological order of the graph nodes is defined as follow:
    - For each directed edge `A -> B` in graph, A must before B in the order list.
    - The first node in the order can be any node in the graph with no nodes direct to it.
    - Find any topological order for the given graph.
    - You can assume that there is at least one topological order in the graph.

    ``` 
    Clarification
    Learn more about representation of graphs
    ```

- **Example**
    - For graph as follow:

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThE9AgZZszyhwe0o9qpp3VyizdIj9kWwMY50HiQEysXvkSLsoZ)

    - The topological order can be:

```
[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
```

- **Challenge**
    - Can you do it in both BFS and DFS?



## Solution

思路：  
Topological Sorting (拓扑排序)，考虑图的 `indegree`。最先得到的 `node` 一定是 `indegree == 0` 的 node。 可以用 `HashMap` 实现 `node -> indegree` 这个关系。 其次，如果得到了第一个 `node`， 那么它的 `neighbors` 的 `indegree` 要减小 `1`，这样才可以让算法继续跑下去。

考虑 `BFS+Queue`

### Code

```java
/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) {
 *         label = x;
 *         neighbors = new ArrayList<DirectedGraphNode>();
 *     }
 * };
 */

public class Solution {
    /*
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        // write your code here
        ArrayList<DirectedGraphNode> result = new ArrayList<>();
        if (graph == null) return result;

        // Initialization: all nodes indegree is 0
        HashMap<DirectedGraphNode, Integer> indegree = new HashMap<>();
        for (DirectedGraphNode node : graph) {
            indegree.put(node, 0);
        }

        // Update all the nodes' indegree
        for (DirectedGraphNode node : graph) {
            for (DirectedGraphNode neighbor: node.neighbors) {
                indegree.put(neighbor, indegree.get(neighbor) + 1);
            }
        }

        // Queue for BFS
        Queue<DirectedGraphNode> queue = new LinkedList<>();

        for (DirectedGraphNode node : graph) {
            if (indegree.get(node) == 0) {
                queue.add(node);
            }
        }

        // BFS
        while (!queue.isEmpty()) {

            // pop the first node
            DirectedGraphNode node = queue.poll();
            result.add(node);

            // decrese indegree of this node's neighbors
            for (DirectedGraphNode neighbor : node.neighbors) {
                indegree.put(neighbor, indegree.get(neighbor) - 1);

                // if indegree of neighbor is 0 again, add to the queue
                if (indegree.get(neighbor) == 0) {
                    queue.add(neighbor);
                }
            }

        }

        return result;

    }
}
```

**九章的题解：**

```java
/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
 * };
 */
public class Solution {
    /**
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */    
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        // write your code here
        ArrayList<DirectedGraphNode> result = new ArrayList<DirectedGraphNode>();
        HashMap<DirectedGraphNode, Integer> map = new HashMap();
        for (DirectedGraphNode node : graph) {
            for (DirectedGraphNode neighbor : node.neighbors) {
                if (map.containsKey(neighbor)) {
                    map.put(neighbor, map.get(neighbor) + 1);
                } else {
                    map.put(neighbor, 1); 
                }
            }
        }
        Queue<DirectedGraphNode> q = new LinkedList<DirectedGraphNode>();
        for (DirectedGraphNode node : graph) {
            if (!map.containsKey(node)) {
                q.offer(node);
                result.add(node);
            }
        }
        while (!q.isEmpty()) {
            DirectedGraphNode node = q.poll();
            for (DirectedGraphNode n : node.neighbors) {
                map.put(n, map.get(n) - 1);
                if (map.get(n) == 0) {
                    result.add(n);
                    q.offer(n);
                }
            }
        }
        return result;
    }
}
```


