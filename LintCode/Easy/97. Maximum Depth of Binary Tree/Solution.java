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
     * @param root: The root of binary tree.
     * @return: An integer
     */
     
    private int depth = 0;
    
    public int maxDepth(TreeNode root) {
        // write your code here
        traverse(root, 1);
        return depth;
    }
    
    
    private void traverse(TreeNode root, int currDepth) {
        
        if (root == null) return;
    
        if (currDepth > depth) depth = currDepth;
        
        traverse(root.left, currDepth + 1);
        traverse(root.right, currDepth + 1);

    }
    
    
}



public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: An integer
     */
    public int maxDepth(TreeNode root) {
        // write your code here

        // Divide and Conquer

        if (root == null) return 0;

        int LeftDepth = maxDepth(root.left);
        int RightDepth = maxDepth(root.right);

        return Math.max(LeftDepth, RightDepth) + 1;
    }


}
