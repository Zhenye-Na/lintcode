# 126. Max Tree

**Description**

Given an integer array with no duplicates. A max tree building on this array is defined as follow:

```
The root is the maximum number in the array
The left subtree and right subtree are the max trees of the subarray divided by the root number.
Construct the max tree by the given array.
```

**Example**

Example 1:

```
Input: [2, 5, 6, 0, 3, 1]
Output: {6,5,3,2,#,0,1}
Explanation: 
the max tree constructed by this array is:
    6
   / \
  5   3
 /   / \
2   0   1
```

Example 2:

```
Input: [6,4,20]
Output: {20,6,#,#,4}
Explanation： 
     20
     / 
    6
     \
      4
```

**Challenge**

`O(n)` time and memory.


**单调递减栈**

其实这种树叫做笛卡树 (Cartesian tree)。直接递归建树的话复杂度最差会退化到 `O(n^2)`。经典建树方法，用到的是单调堆栈。我们堆栈里存放的树，只有左子树，没有右子树，且根节点最大。

1. 如果新来一个数，比堆栈顶的树根的数小，则把这个数作为一个单独的节点压入堆栈。
2. 否则，不断从堆栈里弹出树，新弹出的树以旧弹出的树为右子树，连接起来，直到目前堆栈顶的树根的数大于新来的数。然后，弹出的那些数，已经形成了一个新的树，这个树作为新节点的左子树，把这个新树压入堆栈。

这样的堆栈是单调的，越靠近堆栈顶的数越小。

最后还要按照（2）的方法，把所有树弹出来，每个旧树作为新树的右子树

```
# stack = [2], push 5 因为 5 > 2, 所以2是5的左儿子, pop 2
# stack = [], push 5
# stack = [5], push 6, 因为 6 > 5，所以5是6的左儿子, pop 5
# stack = [], push 6
# stack = [6], push 0, 因为0 < 6, stack = [6], 所以0是6的右儿子
# stack = [6, 0], push 3, 因为3 > 0, 所以0是3的左儿子， pop 0
# stack = [6], 所以3是6的右儿子， push 3
# stack = [6, 3], push 1, 因为1 < 3，所以1是3的右儿子
```

*解法 1*

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
     * @param A: Given an integer array with no duplicates.
     * @return: The root of max tree.
     */
    public TreeNode maxTree(int[] A) {
        // write your code here
        if (A == null || A.length == 0) {
            return null;
        }

        Stack<TreeNode> stack = new Stack<>();
        for (int i = 0; i < A.length; i++) {
            // 遍历 A 的每个元素, 创造结点 node
            TreeNode node = new TreeNode(A[i]);

            // 将 stack 中小于当前结点的结点都 pop 出来, 存为当前结点的左子树
            while (!stack.isEmpty() && node.val >= stack.peek().val) {
                node.left = stack.pop();
            }

            // 如果 stack 仍非空, 剩下的结点一定大于 node, 所以将 node 存为 stack 中结点的右子树;
            // 如果栈中有大于等于2个元素, 栈顶节点自身的右子树, 现在变成了 node 的左子树
            // 栈不空, 栈中还有比遍历到的节点值更大的节点, 那么就要把 node 变成 栈顶节点的右子树
            if (!stack.isEmpty()) {
                stack.peek().right = node;
            }

            // stack中存放结点的顺序为: 底部为完整的 max tree, 从下向上是下一层孩子结点的备份, 顶部是当前结点的备份
            stack.push(node);
        }

        TreeNode root = stack.pop();
        while (!stack.isEmpty()) {
            root = stack.pop();
        }
        return root;
    }
}
```

*解法 2*

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
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        if not A:
            return None
            
        nodes = [TreeNode(num) for num in A + [sys.maxsize]]
        stack = []
        for index, num in enumerate(A + [sys.maxsize]):
            while stack and A[stack[-1]] < num:
                top = stack.pop()
                left = A[stack[-1]] if stack else sys.maxsize
                if left < num:
                    nodes[stack[-1]].right = nodes[top]
                else:
                    nodes[index].left = nodes[top]
            
            stack.append(index)

        # sys.maxsize 's left child is the maximum number
        return nodes[-1].left
```

**DFS**

TLE 过不了, 练练思想

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
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        # write your code here
        if not A or len(A) == 0:
            return None

        return self._findMaxTree(0, len(A) - 1, A)

    def _findMaxTree(self, start, end, A):
        if start > end:
            return None

        if start == end:
            return TreeNode(A[start])

        maxVal = max(A[start:end + 1])
        maxValIdx = A[start:end + 1].index(maxVal) + start

        root = TreeNode(maxVal)
        root.left = self._findMaxTree(start, maxValIdx - 1, A)
        root.right = self._findMaxTree(maxValIdx + 1, end, A)

        return root
```
