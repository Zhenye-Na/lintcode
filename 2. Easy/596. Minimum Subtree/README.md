# 596. Minimum Subtree

- **Description**
    - Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
- **Example**
    - Given a binary tree:
    
    ```
         1
       /   \
     -5     2
     / \   /  \
    0   2 -4  -5
    ```
    
    - return the node 1.

> LintCode will print the subtree which root is your return node.
>
> It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

## Solution

**Divide & Conquer**

- 首先: 无脑丢给左右子树，别管他是什么，想像成程序走到了左下角的子树的位置
- 然后: 再写找到了这棵子树, 你要对他进行什么操作

### Divide & Conquer

#### Python

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def __init__(self):
        self.summation = sys.maxint
        self.node      = None

    def findSubtree(self, root):
        # write your code here
        self.helper(root)
        return self.node

    def helper(self, root):
        if not root:
            return 0

        # Divide & Conquer
        left  = self.helper(root.left)
        right = self.helper(root.right)

        # if current subtree sum is less than flobal minimum, update it
        if left + right + root.val < self.summation:
            self.node      = root
            self.summation = left + right + root.val

        # else return subtree sum
        return left + right + root.val
```

#### Java

```java
/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

// version 1 : traverse + divide conquer
public class Solution {
    private TreeNode subtree = null;
    private int subtreeSum = Integer.MAX_VALUE;
    /**
     * @param root the root of binary tree
     * @return the root of the minimum subtree
     */
    public TreeNode findSubtree(TreeNode root) {
        helper(root);
        return subtree;
    }

    private int helper(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int sum = helper(root.left) + helper(root.right) + root.val;
        if (sum <= subtreeSum) {
            subtreeSum = sum;
            subtree    = root;
        }
        return sum;
    }
}



// version 2: Pure divide conquer
class ResultType {
    public TreeNode minSubtree;
    public int sum, minSum;
    public ResultType(TreeNode minSubtree, int minSum, int sum) {
        this.minSubtree = minSubtree;
        this.minSum     = minSum;
        this.sum        = sum;
    }
}

public class Solution {
    /**
     * @param root the root of binary tree
     * @return the root of the minimum subtree
     */
    public TreeNode findSubtree(TreeNode root) {
        ResultType result = helper(root);
        return result.minSubtree;
    }

    public ResultType helper(TreeNode node) {
        if (node == null) {
            return new ResultType(null, Integer.MAX_VALUE, 0);
        }

        ResultType leftResult  = helper(node.left);
        ResultType rightResult = helper(node.right);

        ResultType result = new ResultType(
            node,
            leftResult.sum + rightResult.sum + node.val,
            leftResult.sum + rightResult.sum + node.val
        );

        if (leftResult.minSum <= result.minSum) {
            result.minSum = leftResult.minSum;
            result.minSubtree = leftResult.minSubtree;
        }

        if (rightResult.minSum <= result.minSum) {
            result.minSum = rightResult.minSum;
            result.minSubtree = rightResult.minSubtree;
        }

        return result;
    }
}
```
