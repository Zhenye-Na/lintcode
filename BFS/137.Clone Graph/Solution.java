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
        if (node == null) {
            return null;
        }

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