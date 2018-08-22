# 137. Clone Graph

- **Description**
    - Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
    - How we serialize an undirected graph:
        - Nodes are labeled uniquely.
        - We use `#` as a separator for each node, and , as a separator for node label and each neighbor of the node.
        - As an example, consider the serialized graph `{0,1,2#1,2#2,2}`.
        - The graph has a total of three nodes, and therefore contains three parts as separated by `#`.
        - First node is labeled as `0`. Connect node `0` to both nodes `1` and `2`.
        - Second node is labeled as `1`. Connect node `1` to node `2`.
        - Third node is labeled as `2`. Connect node `2` to node `2` (itself), thus forming a self-cycle.
    - Visually, the graph looks like the following:

    ```
       1
      / \
     /   \
    0 --- 2
         / \
         \_/
    ```

- **Example**
    - return a deep copied graph.


## Solution

根据 `starter code` 可以发现 `input argument` 只有一个 `node`， 所以我们要根据这一个 `node` 来 `copy` 整张图。

考虑 `BFS+Queue`

- 首先从 `node` 遍历整张图，并且复制每一个节点
- 把原图的 `next` 复制到 新图中



### Code

```java
/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */


public class Solution {
    /*
     * @param node: A undirected graph node
     * @return: A undirected graph node
     */
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        // write your code here
        if (node == null) return null;

        // Get all the nodes from input    
        List<UndirectedGraphNode> initialGraph = getGraphNodes(node);

        // Copy nodes
        HashMap<UndirectedGraphNode, UndirectedGraphNode> mapping = new HashMap<>();
        for (UndirectedGraphNode currNode : initialGraph) {
            mapping.put(currNode, new UndirectedGraphNode(currNode.label));
        }
        
        // Copy edges
        for (UndirectedGraphNode initialNode : initialGraph) {
            for (UndirectedGraphNode neighbor : initialNode.neighbors) {
                mapping.get(initialNode).neighbors.add(mapping.get(neighbor));
            }
        }

        return mapping.get(node);
    }

    
    private List<UndirectedGraphNode> getGraphNodes(UndirectedGraphNode node) {

        // BFS to get all nodes
        List<UndirectedGraphNode> graph = new ArrayList<>();
        Set<UndirectedGraphNode> history = new HashSet<>();
        Queue<UndirectedGraphNode> queue = new LinkedList<>();
        queue.offer(node);
        history.add(node);
        
        while (!queue.isEmpty()) {
            
            UndirectedGraphNode tmpNode = queue.poll();
            graph.add(tmpNode);

            for (UndirectedGraphNode neighbor : tmpNode.neighbors) {
                if (!history.contains(neighbor)) {
                    queue.offer(neighbor);
                    history.add(neighbor);
                }
            }
            
        }
        return graph;
    }

}
```
