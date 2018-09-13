# 73. Construct Binary Tree from Preorder and Inorder Traversal

Description
Given preorder and inorder traversal of a tree, construct the binary tree.

You may assume that duplicates do not exist in the tree.

Example
Given in-order `[1,2,3]` and pre-order `[2,1,3]`, return a tree:

```
  2
 / \
1   3
```



```java
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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // write your code here
        return helper(0, 0, inorder.length - 1, preorder, inorder);
    }

    private TreeNode helper(int preStart, int inStart, int inEnd, int[] preorder, int[] inorder) {
        if (preStart > preorder.length - 1 || inStart > inEnd) {
            return null;
        }
        TreeNode root = new TreeNode(preorder[preStart]);
        int rootIndex = 0;
        for (int i = inStart; i <= inEnd; i++) {
            if (root.val == inorder[i]) {
                rootIndex = i;
            }
        }

        root.left = helper(preStart + 1, inStart, rootIndex - 1, preorder, inorder);
        root.right = helper(preStart + 1 + rootIndex - inStart, rootIndex + 1, inEnd, preorder, inorder);
        return root;
    }
}
```
