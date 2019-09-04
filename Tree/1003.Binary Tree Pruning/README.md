# 1003. Binary Tree Pruning

**Description**

Given the head node root of a binary tree, where additionally every node's value is either a `0` or a `1`.

Return this tree where every subtree (of the given tree) not containing a `1` has been removed.

(Recall that the subtree of a node `X` is `X`, plus every node that is a descendant of `X`.)

```
The binary tree will have at most 100 nodes.
The value of each node will only be 0 or 1.
```

**Example**

Example 1:

```
Input: {1,#,0,0,1}
Output: {1,#,0,#,1}
Explanation: 
  Only the red nodes satisfy the property "every subtree not containing a 1".
  The diagram on the right represents the answer.
```

![](https://lintcode-media.s3.amazonaws.com/problem/1028_2.png)

Example 2:

```
Input: {1,0,1,0,0,0,1}
Output: {1,#,1,#,1}
```

![](https://lintcode-media.s3.amazonaws.com/problem/1028_1.png)

Example 3:

```
Input: {1,1,0,1,1,0,1,0}
Output: {1,1,0,1,1,#,1}
```

![](https://lintcode-media.s3.amazonaws.com/problem/1028.png)


做一次DFS即可, DFS的同时删除值为0的节点.

代码看起来十分简练, 重点在于最后return时的判断:

如果该节点是值为0的叶子节点, 就删除它. 按照这样递归的实现顺序, 节点被删除时总是叶子节点.

```java
/**
* This reference program is provided by @jiuzhang.com
* Copyright is reserved. Please indicate the source for forwarding
*/

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
     * @param root: the root
     * @return: the same tree where every subtree (of the given tree) not containing a 1 has been removed
     */
    public TreeNode pruneTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        root.left = pruneTree(root.left);
        root.right = pruneTree(root.right);
        return root.val == 0 && root.left == null && root.right == null ? null : root;
    }
}
```