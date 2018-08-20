# 661. Convert BST to Greater Tree
Description
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Have you met this question in a real interview?  
Example

```
Given a binary search Tree `{5,2,13}｀:

              5
            /   \
           2     13


Return the root of new tree



             18
            /   \
          20     13
```


## Solution

### Inorder-Traversal

- Time  `O(n)`
- Space `O(n)`


```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """
    def convertBST(self, root):
        # write your code here
        traverse = self.inorderTraversal(root)
        self.updateNode(traverse)
        return root

    def inorderTraversal(self, root):
        result = []
        if root is None:
            return result

        left  = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        result.extend(left)
        result.append(root)
        result.extend(right)

        return result

    def updateNode(self, traverse):
        left, right = len(traverse) - 2, len(traverse) - 1
        while left >= 0:
            traverse[left].val += traverse[right].val
            left  -= 1
            right -= 1

```


### Solution 2

- Time  `O(n)`
- Space `O(1)`

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """
    def convertBST(self, root):
        # write your code here
        self.sum = 0
        self.helper(root)
        return root

    def helper(self, root):
        if root is None:
            return

        if root.right:
            self.helper(root.right)

        self.sum += root.val
        root.val = self.sum
        if root.left:
            self.helper(root.left)
```


### DFS


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

// version: 高频题班
public class Solution {
    /**
     * @param root the root of binary tree
     * @return the new root
     */
    int sum = 0;

    void dfs(TreeNode cur) {
        if (cur == null) {
            return;
        }
        dfs(cur.right);
        sum += cur.val;
        cur.val = sum;
        dfs(cur.left);
    }

    public TreeNode convertBST(TreeNode root) {
        // Write your code here
        dfs(root);
        return root;
    }
}
```
