# 85. Insert Node in a Binary Search Tree

- **Description**
    - Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.
    - You can assume there is no duplicate values in this tree + node.
- **Example**
    - Given binary search tree as follow, after Insert node 6, the tree should be:

    ```
      2             2
     / \           / \
    1   4   -->   1   4
       /             / \
      3             3   6
    ```

- **Challenge**
    - Can you do it without recursion?


## Solution

### Traverse

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
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node
        self.helper(root, node)
        return root


    def helper(self, root, node):
        if node.val >= root.val:
            if root.right:
                self.helper(root.right, node)
            else:
                root.right = node
                return
        else:
            if root.left:
                self.helper(root.left, node)
            else:
                root.left = node
                return
```


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
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node

        dummy = root
        while dummy:
            if node.val >= dummy.val:
                if dummy.right:
                    dummy = dummy.right
                else:
                    dummy.right = node
                    break
            else:
                if dummy.left:
                    dummy = dummy.left
                else:
                    dummy.left = node
                    break

        return root
```


```java
/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
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
     * @param root: The root of the binary search tree.
     * @param node: insert this node into the binary search tree
     * @return: The root of the new binary search tree.
     */
    public TreeNode insertNode(TreeNode root, TreeNode node) {
        if (root == null) {
            return node;
        }
        if (root.val > node.val) {
            root.left = insertNode(root.left, node);
        } else {
            root.right = insertNode(root.right, node);
        }
        return root;
    }
}
```
