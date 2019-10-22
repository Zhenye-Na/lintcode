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