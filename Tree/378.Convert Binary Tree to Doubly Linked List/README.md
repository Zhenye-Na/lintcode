# 378. Convert Binary Tree to Doubly Linked List

**Description**

Convert a binary tree to doubly linked list with *in-order traversal*.

**Example**

Example 1:

```
Input:
	    4
	   / \
	  2   5
	 / \
	1   3		

Output: 1<->2<->3<->4<->5
```

Example 2:

```
Input:
	    3
	   / \
	  4   1

Output:4<->3<->1
```

**Divide Conquer**

`O(n)` Space

先中序遍历出来, 在创建一个 Doubly Linked List

```python
"""
Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = nextDefinition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        # write your code here
        if not root:
            return None
        traversal = self._inorderTraversal(root)

        parent_node = DoublyListNode(traversal[0])
        first = parent_node

        for i in range(1, len(traversal)):
            current_node = DoublyListNode(traversal[i])
            parent_node.next = current_node
            current_node.prev = parent_node
            parent_node = parent_node.next

        return first

    def _inorderTraversal(self, root):
        if not root:
            return []

        left = self._inorderTraversal(root.left)
        right = self._inorderTraversal(root.right)

        return left + [root.val] + right

```