/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param root: A tree
     * @return: buttom-up level order a list of lists of integer
     */
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        // write your code here
        
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        if (root == null) return results;
        
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);

        // BFS using queue
        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);

                if (node.left != null)  queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            
            results.add(0, level);
        }

        return results;
    }
}