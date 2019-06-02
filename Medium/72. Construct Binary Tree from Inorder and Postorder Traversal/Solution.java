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
     * @param inorder: A list of integers that inorder traversal of a tree
     * @param postorder: A list of integers that postorder traversal of a tree
     * @return: Root of a tree
     */
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        // write your code here
        int[] postEnd = new int[1];
        postEnd[0] = postorder.length - 1;
        return helper(postEnd, 0, inorder.length - 1, inorder, postorder);
    }

    private TreeNode helper(int[] postEnd, int startIn, int endIn, int[] inorder, int[] postorder) {

        if (postEnd[0] < 0 || startIn > endIn){
            return null;
        }

        //pop off end of postOrder
        int val = postorder[postEnd[0]];

        int mid = 0;
        for (int i = startIn; i <= endIn; i++){
            if (inorder[i] == val){
                mid = i;
                break;
            }
        }

        TreeNode root = new TreeNode(val);
        postEnd[0] = postEnd[0] - 1;
        root.right = helper(postEnd, mid + 1, endIn, inorder, postorder);
        root.left  = helper(postEnd, startIn, mid - 1, inorder, postorder);

        return root;
    }

}
