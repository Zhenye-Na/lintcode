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
     * @return: the root of the minimum subtree
     */
    
    private int minimum = Integer.MAX_VALUE;
    private TreeNode node;
    
    public TreeNode findSubtree(TreeNode root) {
        // write your code here
        int sum = helper(root);
        return node;
    }

    // Traverse to get the sum
    private int helper(TreeNode root) {
        
        // 当前节点是 null， 返回 0
        if (root == null) return 0;
        
        // 遍历 左右子树，求和
        int left = helper(root.left);
        int right = helper(root.right);

        int sum = left + right + root.val;
        
        // 如果当前子树 sum 比 之前最小值 还小，更新 sum 和 node
        if (sum < minimum) {
            minimum = sum;
            node = root;
        }

        return sum;

    }

}