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
    /*
     * @param root: the root of tree
     * @return: the max node
     */
    public TreeNode maxNode(TreeNode root) {
        // write your code here
        
        if (root == null) return null;
        
        TreeNode res = root;
        TreeNode lres = maxNode(root.left);
        TreeNode rres = maxNode(root.right);
        
        // if reach leaves, change leaves (null) to empty nodes
        if (lres == null) lres = new TreeNode(Integer.MIN_VALUE);
        if (rres == null) rres = new TreeNode(Integer.MIN_VALUE);
 
        // get the max value
        if (lres.val > res.val)
            res = lres;
        if (rres.val > res.val)
            res = rres;

        return res;

    }
}