# 376. Binary Tree Path Sum

## Table of Contents

- [Solution 1](solution-1)
    - [Code](#code-1)
- [Solution 2](solution-2)
    - [Code](#code-2)
- [Solution 3](solution-3)
    - [Code](#code-3)

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

#### Code 1

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
            traverse(root.left, left);
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
从 solution 1 中可以明显发现其中的缺点，并不需要获得所有的路径，只有在计算中发现 `sum == target` ，才把他加进 results 当中，并且不需要最后 `for loop` 那一步。 用到了 ResultType，同时记录 path 和 当前 sum 值。 时间复杂度有很大提高。

```
100% test cases passed, Total runtime 2326 ms
Your submission beats 62.80% Submissions!
```

#### Code 2

```java
class ResultType {
    public int sum;
    public List<Integer> path;
    public ResultType(int sum, List<Integer> path) {
        this.sum = sum;
        this.path = path;
    }
}

public class Solution {
    /*
     * @param root: the root of binary tree
     * @param target: An integer
     * @return: all valid paths
     */
    private List<List<Integer>> results = new ArrayList<List<Integer>>();

    public List<List<Integer>> binaryTreePathSum(TreeNode root, int target) {
        // write your code here
        if (root == null) return results;
        
        List<Integer> path = new ArrayList<>();
        path.add(root.val);
        ResultType res = new ResultType(root.val, path);

        helper(root, target, res);
        System.out.println(results);
        return results;
        
    }

    private ResultType helper(TreeNode root, int target, ResultType res) {

        // leaf nodes
        if (root.left == null && root.right == null) {
            if (res.sum == target) {
                List<Integer> curr = new ArrayList<>(res.path);
                results.add(curr);
            }
            return res;
        }

        // Split
        if (root.left != null) {
            List<Integer> leftpath = new ArrayList<>(res.path); // [1] [1,2]
            leftpath.add(root.left.val); // [1,2] [1,2,2]
            ResultType left = new ResultType(res.sum + root.left.val, leftpath); // [1+2], [1,2]     [3+2],[1,2,2]
            helper(root.left, target, left);
        }

        if (root.right != null) {
            List<Integer> rightpath = new ArrayList<>(res.path);
            rightpath.add(root.right.val);
            ResultType right = new ResultType(res.sum + root.right.val, rightpath);
            helper(root.right, target, right);
        }

        return res;
    }

}
```


### Solution 3

九章的答案，写的十分简短，非常棒，还要继续学习

```java
public class Solution {
    /*
     * @param root: the root of binary tree
     * @param target: An integer
     * @return: all valid paths
     */

    public List<List<Integer>> binaryTreePathSum(TreeNode root, int target) {
        // write your code here
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;

        ArrayList<Integer> path = new ArrayList<Integer>();
        path.add(root.val);

        helper(root, path, root.val, target, result);
        return result;
    }

    private void helper(TreeNode root,
                        ArrayList<Integer> path,
                        int sum,
                        int target,
                        List<List<Integer>> result) {

        // leaf nodes
        if (root.left == null && root.right == null) {
            if (sum == target) {
                result.add(new ArrayList<Integer>(path));
            }
        }


        // go left
        if (root.left != null) {
            path.add(root.left.val);
            helper(root.left, path, sum + root.left.val, target, result);
            path.remove(path.size() - 1);
        }

        // go right
        if (root.right != null) {
            path.add(root.right.val);
            helper(root.right, path, sum + root.right.val, target, result);
            path.remove(path.size() - 1);
        }

    }

}
```




