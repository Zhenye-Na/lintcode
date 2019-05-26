public class Solution {
    /**
     * @param graph: the given undirected graph
     * @return:  return true if and only if it is bipartite
     */
    public boolean isBipartite(int[][] graph) {
        // Write your code here
        //BFS
        // 0(not meet), 1(black), 2(white)
        int[] visited = new int[graph.length];

        for (int i = 0; i < graph.length; i++) {
            if (graph[i].length != 0 && visited[i] == 0) {

                visited[i] = 1;
                Queue<Integer> q = new LinkedList<>();
                q.offer(i);

                while(!q.isEmpty()) {
                    int current = q.poll();
                    for (int c: graph[current]) {

                            if (visited[c] == 0) {
                                visited[c] = (visited[current] == 1) ? 2 : 1;
                                q.offer(c);
                            } else {
                                if (visited[c] == visited[current]) {
                                    return false;
                                }
                            }
                    }
                }                        
                
            }
        }

        return true;
    }
}