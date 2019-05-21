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






// DFS Implemetation

/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
 * };
 */

public class Solution {
    /*
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        // write your code here
        if (graph == null || graph.size() == 0) {
            return new ArrayList<DirectedGraphNode>();
        }
        LinkedList<DirectedGraphNode> result = new LinkedList<>();
        Set<DirectedGraphNode> gray = new HashSet<>();
        Set<DirectedGraphNode> dark = new HashSet<>();
        for (DirectedGraphNode node : graph) {
            if (!gray.contains(node) && !dark.contains(node)) {
                dfs(node, gray, dark, result);
            }
        }
        return new ArrayList<DirectedGraphNode>(result);
    }
    
    void dfs(DirectedGraphNode node, Set<DirectedGraphNode> gray, Set<DirectedGraphNode> dark, LinkedList<DirectedGraphNode> result) {
        gray.add(node);
        for (DirectedGraphNode child : node.neighbors) {
            if (!gray.contains(child) && !dark.contains(child)) {
                dfs(child, gray, dark, result);
            }
        }
        dark.add(node);
        gray.remove(node);
        result.addFirst(node);
    }
}