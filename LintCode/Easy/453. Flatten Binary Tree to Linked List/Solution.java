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
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */

    private TreeNode prevNode = null;
    
    public void flatten(TreeNode root) {
        // write your code here
        
        if (root == null) return;
        
        // last node you traversed
        if (prevNode != null) {
            prevNode.left = null;
            prevNode.right = root;

        }
        
        // The node just traversed
        prevNode = root;
        
        // keep the right subtree
        TreeNode currRight = root.right;
        
        // traverse subtree
        flatten(root.left);
        flatten(currRight);

    }

}