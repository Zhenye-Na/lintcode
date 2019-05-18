# 69. Binary Tree Level Order Traversal

**Description**

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

```
The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20.
```


**Example**

Example 1:

```
Input: {1,2,3}
Output: [[1],[2,3]]
Explanation：
  1
 / \
2   3
it will be serialized {1,2,3}
level order traversal
```

Example 2:

```
Input: {1,#,2,3}
Output: [[1],[2],[3]]
Explanation：
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
level order traversal
```

**Challenge**

- Challenge 1: Using only 1 queue to implement it.
- Challenge 2: Use DFS algorithm to do it.


**BFS + Queue**

- Time Complexity `O(n)`: since we visited each node once
- Space Complexity `O(n)`: it depends on the size of the Queue. The worst case will be `n/2` which is the number of leaves. 


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
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        result = []
        q      = []

        if root is None:
            return result

        q.append(root)
        while q:
            size = len(q)
            level  = []

            for i in range(size):

                node = q.pop(0)
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)

        return result
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
     * @param root: A Tree
     * @return: Level order a list of lists of integer
     */
    public List<List<Integer>> levelOrder(TreeNode root) {
        // write your code here

        // List results = new ArrayList<>();
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        Queue<TreeNode> queue = new LinkedList<>();

        if (root == null) return results;
        queue.add(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> level = new ArrayList<>();

            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);

                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }

            results.add(level);
        }

        return results;
    }
}
```

**DFS**

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
     * @param root: The root of binary tree.
     * @return: Level order a list of lists of integer
     */
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();

        if (root == null) {
            return results;
        }

        int maxLevel = 0;
        while (true) {
            List<Integer> level = new ArrayList<Integer>();
            dfs(root, level, 0, maxLevel);
            if (level.size() == 0) {
                break;
            }

            results.add(level);
            maxLevel++;
        }
        return results;
    }

    private void dfs(TreeNode root,
                     List<Integer> level,
                     int curtLevel,
                     int maxLevel) {
        if (root == null || curtLevel > maxLevel) {
            return;
        }

        if (curtLevel == maxLevel) {
            level.add(root.val);
            return;
        }

        dfs(root.left, level, curtLevel + 1, maxLevel);
        dfs(root.right, level, curtLevel + 1, maxLevel);
    }
}
```
