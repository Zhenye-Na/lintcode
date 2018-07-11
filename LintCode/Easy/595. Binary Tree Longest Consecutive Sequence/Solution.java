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
     * @param root: the root of binary tree
     * @return: the length of the longest consecutive sequence path
     */

    private int length = 0;
    public int longestConsecutive(TreeNode root) {
        // write your code here
        helper(root);
        return length;
    }

    // Definition: find longest consecutive sequence in subtree
    private int helper(TreeNode root) {
        // Exit
        if (root == null) {
            return 0;
        }

        // Split
        int left = helper(root.left);
        int right = helper(root.right);

        int sublength = 1; // 记录当前根节点

        // 左子树非空，并且 根节点 与 左叶子节点值 相差 1
        if (root.left != null && root.val - root.left.val == -1) {
            sublength = Math.max(sublength, left + 1);
        }
        // 右子树非空，并且 根节点 与 右叶子节点值 相差 1
        if (root.right != null && root.val - root.right.val == -1) {
            sublength = Math.max(sublength, right + 1);
        }
        // 更新 全局变量
        if (sublength > length) {
            length = sublength;
        }
        // 返回 subtree 的长度
        return sublength;
    }
    
    
}