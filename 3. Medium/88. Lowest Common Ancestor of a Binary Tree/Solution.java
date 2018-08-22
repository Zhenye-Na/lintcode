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
     * @param root: The root of the binary search tree.
     * @param A: A TreeNode in a Binary.
     * @param B: A TreeNode in a Binary.
     * @return: Return the least common ancestor(LCA) of the two nodes.
     */
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        // write your code here

        // Exit
        if (root == null || A == root || B == root) {
            return root;
        }

        // Split
        TreeNode left = lowestCommonAncestor(root.left, A, B);
        TreeNode right = lowestCommonAncestor(root.right, A, B);
        
        // We find in left tree and right tree
        if (left != null && right != null) {
            return root;
        }

        // We find in left subtree
        if (left != null) {
            return left;
        }

        // we find in right subtree
        if (right != null) {
            return right;
        }

        // We did not find target
        return null;
    }
}