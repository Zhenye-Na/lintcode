# 376. Binary Tree Path Sum

## Table of Contents

- [Solution](#solution)
    - [Solution 1](solution-1)
        - [Code](#code)
    - [Solution 2](solution-2)
        - [Code](#code)

- **Description**
    - Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.
    - A valid path is from root node to any of the leaf nodes.
- **Example**
    - Given a binary tree, and target = 5:

    ```
         1
        / \
       2   4
      / \
     2   3
    ```

    - return

    ```
    [
      [1, 2, 2],
      [1, 4]
    ]
    ```

## Solution

### Solution 1

这道题 求子树 `val` 之和等于 `target` 的所有子树，且必须从 `root` 出发到 `leaf` 为止。

首先想到的解法是暴力算得从 `root` 出发到 `leaf` 结束的所有路径，然后 `for loop` 一遍，选出 `sum == target` 的路径，放进 `results` 当中即可

**缺点**：太TM慢了

```
100% test cases passed, Total runtime 4029 ms  
Your submission beats 3.60% Submissions!
```

#### Code

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
    /*
     * @param root: the root of binary tree
     * @param target: An integer
     * @return: all valid paths
     */
    
    List<List<Integer>> paths = new ArrayList<List<Integer>>();
    public List<List<Integer>> binaryTreePathSum(TreeNode root, int target) {
        // write your code here

        List<Integer> path = new ArrayList<Integer>();
        if (root == null) return paths;

        traverse(root, path);

        List<List<Integer>> results = new ArrayList<List<Integer>>();
        for (List<Integer> list : paths) {
            int sum  = list.stream().mapToInt(Integer::intValue).sum();
            if (sum == target) {
                results.add(list);
            }
        }

        return results;
    }

    // Definition: find all paths in subtrees
    private void traverse(TreeNode root, List<Integer> path) {
        // Exit when traverse to leaf nodes
        if (root.left == null && root.right == null) {
            List<Integer> currPath = new ArrayList<> (path);
            currPath.add(root.val);
            paths.add(currPath);
            return;
        }

        // Split
        if (root.left != null) {
            List<Integer> left = new ArrayList<>(path);
            left.add(root.val);
            traverse(root.left, left); // [1]  [1,2]
        }

        if (root.right != null) {
            List<Integer> right = new ArrayList<>(path);
            right.add(root.val);
            traverse(root.right, right);
        }

    }

}
```

### Solution 2
从 solution 1 中可以明显发现其中的缺点，并不需要获得所有的路径，只有在计算中发现 `sum == target` ，才把他加进 results 当中，并且不需要最后 `for loop` 那一步。

#### Code

```java

```







