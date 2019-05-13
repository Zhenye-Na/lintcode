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
    private int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        // write your code here
        helper(root);
        return max;
    }
    
    private int helper(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int left = helper(root.left);
        int right = helper(root.right);
        
        int curr_max = Math.max(Math.max(left + root.val, right + root.val), root.val);
        max = Math.max(max, Math.max(curr_max, root.val + left + right));
        return curr_max;
    }
}