# 70. Binary Tree Level Order Traversal II

- **Description**
    - Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
- **Example**
    - Given binary tree `{3,9,20,#,#,15,7}`,

    ```
        3
       / \
      9  20
        /  \
       15   7
    ```

    - return its bottom-up level order traversal as:

        ```java
        [
          [15,7],
          [9,20],
          [3]
        ]
        ```

## Solution

### `Queue + Stack`

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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        queue  = []
        stack = []

        if root is None:
            return stack

        queue.append(root)
        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                # pop queue
                node = queue.pop(0)
                level.insert(0, node.val)

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

            stack.append(level)

        return stack[::-1]

```

### `BFS` + `Queue` + `list.insert(0, level)` / `list.add(0, level)`

#### Python

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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        queue  = []
        result = []

        if root is None:
            return result

        queue.append(root)
        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                # pop queue
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.insert(0, level)

        return result

```

#### Java

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
     * @param root: A tree
     * @return: buttom-up level order a list of lists of integer
     */
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        // write your code here

        List<List<Integer>> results = new ArrayList<List<Integer>>();
        if (root == null) return results;

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);

        // BFS using queue
        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);

                if (node.left != null)  queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }

            results.add(0, level);
        }

        return results;
    }
}
```
