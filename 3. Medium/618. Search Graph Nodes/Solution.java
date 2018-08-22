/**
 * Definition for graph node.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { 
 *         label = x; neighbors = new ArrayList<UndirectedGraphNode>(); 
 *     }
 * };
 */


public class Solution {
    /*
     * @param graph: a list of Undirected graph node
     * @param values: a hash mapping, <UndirectedGraphNode, (int)value>
     * @param node: an Undirected graph node
     * @param target: An integer
     * @return: a node
     */
    public UndirectedGraphNode searchNode(ArrayList<UndirectedGraphNode> graph,
                                          Map<UndirectedGraphNode, Integer> values,
                                          UndirectedGraphNode node,
                                          int target) {
        // write your code here
        HashSet<UndirectedGraphNode> history = new HashSet<>();
        Queue<UndirectedGraphNode> queue = new LinkedList<>();
        queue.offer(node);
        history.add(node);

        while (!queue.isEmpty()) {

            UndirectedGraphNode n = queue.poll();
            if (values.get(n) == target) {
                return n;
            }

            for (UndirectedGraphNode neighbor : n.neighbors) {
                if (!history.contains(neighbor)) {
                    queue.offer(neighbor);
                    history.add(neighbor);
                }
            }

        }

        return null;
    }
}