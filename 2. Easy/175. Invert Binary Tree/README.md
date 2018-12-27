# 175. Invert Binary Tree

- **Description**
    - Invert a binary tree.

- **Example**

    ```
      1         1
     / \       / \
    2   3  => 3   2
       /       \
      4         4
    ```

- **Challenge**
    - Do it in recursion is acceptable, can you do it without recursion?


## Solution

考察二叉树遍历，使用DFS，DFS出口为`当前节点为空`。遍历到当前节点是，将左孩子与右孩子交换即可。

### Java

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
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void invertBinaryTree(TreeNode root) {
        // write your code here
        if (root == null) {
            return;
        }

        // swap left child and right child
        TreeNode tmp = root.left;
        root.left = root.right;
        root.right = tmp;

        // recursively call invertBinaryTree()
        invertBinaryTree(root.left);
        invertBinaryTree(root.right);
    }
}
```