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
    public int alength;
    public int dlength;
    public ResultType(int a, int d) {
        alength = a;
        dlength = d;
    }
}

public class Solution {
    /**
     * @param root: the root of binary tree
     * @return: the length of the longest consecutive sequence path
     */
    // private int asclength;
    // private int dsclength;
    private int length = 0;
    public int longestConsecutive2(TreeNode root) {
        // write your code here
        helper(root);
        return length;
    }

    
    private ResultType helper(TreeNode root) {
        // Exit
        if (root == null) {
            return new ResultType(0, 0);
        }

        // Split
        ResultType left = helper(root.left);    // (1,1) (2,1)
        ResultType right = helper(root.right);  // (0,0) (1,1)
                                                // sublength (2,1)
                                                // length 2

        ResultType sublength = new ResultType(1, 1);

        if (root.left != null) {
            if (root.val + 1 == root.left.val) {
                sublength.alength = Math.max(sublength.alength, left.alength + 1);
            } else if (root.val - 1 == root.left.val) {
                // descending
                sublength.dlength = Math.max(sublength.dlength, left.dlength + 1);
            }
        }

        // if (root.left != null && root.val + 1 == root.left.val) {
        //     // ascending
        //     sublength.alength = Math.max(sublength.alength, left.alength + 1);
        // } else if (root.left != null && root.val - 1 == root.left.val) {
        //     // descending
        //     sublength.dlength = Math.max(sublength.dlength, left.dlength + 1);
        // }

        if (root.right != null) {
            if (root.val + 1 == root.right.val) {
                sublength.alength = Math.max(sublength.alength, right.alength + 1);
            } else if (root.val - 1 == root.right.val) {
                sublength.dlength = Math.max(sublength.dlength, right.dlength + 1);
            }
        }


        // if (root.right != null && root.val + 1 == root.right.val) {
        //     // ascending
        //     sublength.alength = Math.max(sublength.alength, right.alength + 1);
        // } else if (root.right != null && root.val - 1 == root.right.val) {
        //     // descending
        //     sublength.dlength = Math.max(sublength.dlength, right.dlength + 1);
        // }

        // if (root.left != null && root.right != null) {
        // if (root.left != null && root.right != null && root.left.val + 1 == root.val && root.val + 1 == root.right.val) {
        //     length = Math.max(length, left.dlength + right.alength + 1);
        // } else if (root.left != null && root.right != null && root.left.val - 1 == root.val && root.val - 1 == root.right.val) {
        //     length = Math.max(length, left.alength + right.dlength + 1);
        // } else if (root.left != null && root.left.val + 1 == root.val) {
        //     length = Math.max(length, left.dlength + 1);
        // } else if (root.left != null && root.left.val - 1 == root.val) {
        //     length = Math.max(length, left.alength + 1);
        // } else if (root.right != null && root.right.val + 1 == root.val) {
        //     length = Math.max(length, right.dlength + 1);
        // } else if (root.right != null && root.right.val - 1 == root.val) {
        //     length = Math.max(length, right.alength + 1);
        // }
        // // }

        length = Math.max(length, sublength.alength + sublength.dlength - 1);
        return sublength;

    }

}