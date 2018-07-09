# 480. Binary Tree Paths

**Description**  
Given a binary tree, return all root-to-leaf paths.
  
**Example**  
Given the following binary tree:

    ```
       1
     /   \
    2     3
     \
      5
    ```

All root-to-leaf paths are:

    ```
    [
      "1->2->5",
      "1->3"
    ]
    ```
    

## Solution

这道题要求输出从 root 出发 到 leaf 结束的所有路径。String 在Java是 immutable 的， 所以我把它作为一个 argument 传入 helper 函数。

指的注意的是，何时更新你的 result List。只有当当前所在 Node 是 leaf 的时候，当前路径才算结束，这时才把此路径加进 result List 当中。

用到的函数：

```java
public static String valueOf(Object obj)

/**
Returns the string representation of the Object argument.
Parameters:
    obj - an Object.
Returns:
    if the argument is null, then a string equal to "null";
    otherwise, the value of obj.toString() is returned.
*/
```


### Code

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
     * @param root: the root of the binary tree
     * @return: all root-to-leaf paths
     */
    public List<String> binaryTreePaths(TreeNode root) {
        // write your code here
        List<String> result = new ArrayList<>();
        if (root == null) return result;

        helper(root, String.valueOf(root.val), result);
        return result;
    }
    
    private void helper(TreeNode root, String path, List<String> result) {
        
        if (root == null) return;

        if (root.left == null && root.right == null) {
            result.add(path);
            return;
        }
        
        if (root.left != null) {
            helper(root.left, path + "->" + String.valueOf(root.left.val), result);
        }
        if (root.right != null) {
            helper(root.right, path + "->" + String.valueOf(root.right.val), result);   
        }
        
    }
    
}
```
