# 71. Binary Tree Zigzag Level Order Traversal

- **Description**
    - Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
- **Example**
    - Given binary tree `{3,9,20,#,#,15,7}`,

    ```
        3
       / \
      9  20
        /  \
       15   7
    ```

    - return its zigzag level order traversal as:

    ```
    [
      [3],
      [20,9],
      [15,7]
    ]
    ```

## Solution

### `Deque`

该方法利用数据结构双向队列的特点，利用从前端读，从后端读，从前端写，从后端写的交替使用，保证每层数据有序的进入队列中；

算法时间复杂度为 `O(n)`

```java
/**
* 本参考程序来自九章算法，由 @李同学 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

public class Solution {
    /*
     * @param root: A Tree
     * @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
     */
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        // write your code here
        List<List<Integer>> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        Deque<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        boolean isFromLeft = false;
        while(!queue.isEmpty()) {

            int size = queue.size();
            isFromLeft = !isFromLeft;
            List<Integer> list = new ArrayList<>();

            for(int i = 0; i < size; i++) {
                TreeNode node;
                if (isFromLeft) {
                    node = queue.pollFirst();
                } else {
                    node = queue.pollLast();
                }
                list.add(node.val);

                if (isFromLeft) {
                    if (node.left != null) {
                       queue.offerLast(node.left);
                    }
                    if (node.right != null) {
                        queue.offerLast(node.right);
                    }
                } else {
                    if (node.right != null) {
                       queue.offerFirst(node.right);
                    }
                    if (node.left != null) {
                        queue.offerFirst(node.left);
                    }
                }
            }
            result.add(list);
        }

        return result;
    }
}
```

### `Queue + Reverse`

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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        queue  = []
        result = []
        flag = 1

        if not root:
            return result

        queue.append(root)
        while queue:
            level = []
            size  = len(queue)

            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if flag != 1:
                level.reverse()

            flag = -flag
            result.append(level)

        return result

```
