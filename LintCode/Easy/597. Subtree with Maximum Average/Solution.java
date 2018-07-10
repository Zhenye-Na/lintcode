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

class ResultType {
    public int sum;
    public int size;
    public ResultType (int sum, int size) {
        this.sum = sum;
        this.size = size;
    }
}

public class Solution {
    /**
     * @param root: the root of binary tree
     * @return: the root of the maximum average of subtree
     */
    
    private ResultType maxAvg =  null;
    private TreeNode node = null;
    
    public TreeNode findSubtree2(TreeNode root) {
        // write your code here
        ResultType result = helper(root);
        return node;
        
    }

    // Definition: Recursively find maximum average in left subtree and right subtree
    private ResultType helper(TreeNode root) {

        // Exit: 
        if (root == null) {
            return new ResultType(0, 0);
        }

        // Split into subtree
        ResultType left = helper(root.left);
        ResultType right = helper(root.right);

        ResultType result = new ResultType(root.val + left.sum + right.sum,
                                           1 + left.size + right.size);

        // Update maximum average
        if (node == null || maxAvg.sum * result.size < result.sum * maxAvg.size) {
            maxAvg = result;
            node = root;
        }

        return result;
    }
    
}