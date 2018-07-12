# 69. Binary Tree Level Order Traversal

- **Description**
    - Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
- **Example**
    - Given binary tree {3,9,20,#,#,15,7},

    ```
        3
       / \
      9  20
        /  \
       15   7
    ```

    - return its level order traversal as:

    ```
    [
      [3],
      [9,20],
      [15,7]
    ]
    ```

- **Challenge**
    - Challenge 1: Using only 1 queue to implement it.
    - Challenge 2: Use DFS algorithm to do it.

    
    
## Solution

用 BFS+Queue 可以解决


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