# 468. Symmetric Binary Tree

**Description**

Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


**Example**

Example 1:

```
Input: {1,2,2,3,4,4,3}
Output: true
Explanation:
         1
        / \
       2   2
      / \ / \
      3 4 4 3

is a symmetric binary tree.
```

Example 2:

```
Input: {1,2,2,#,3,#,3}
Output: false
Explanation:
         1
        / \
        2  2
        \   \
         3   3

is not a symmetric binary tree.
```

**Challenge**

Can you solve it both recursively and iteratively?


**BFS**

```python
from collections import deque
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree.
    @return: true if it is a mirror of itself, or false.
    """

    def isSymmetric(self, root):
        # write your code here
        if not root:
            return True

        queue = deque([root])
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    level.append(node.left)
                    queue.append(node.left)
                else:
                    level.append(TreeNode(sys.maxsize))

                if node.right:
                    level.append(node.right)
                    queue.append(node.right)
                else:
                    level.append(TreeNode(sys.maxsize))

            for v1, v2 in zip(level, reversed(level)):
                if v1.val != v2.val:
                    return False

        return True

```

**Divide & Conquer**

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
     * @param root, the root of binary tree.
     * @return true if it is a mirror of itself, or false.
     */
    public boolean isSymmetric(TreeNode root) {
        // Write your code here
        if (root == null) {
            return true;
        }
        return check(root.left, root.right);
    }

    private boolean check(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) {
            return true;
        }
        if (root1 == null || root2 == null) {
            return false;
        }
        if (root1.val != root2.val) {
            return false;
        }
        return check(root1.left, root2.right) && check(root1.right, root2.left);
    }
}
```