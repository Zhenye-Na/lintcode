# 106. Convert Sorted List to Binary Search Tree

**Description**

Given a singly linked list where elements are sorted in *ascending order*, convert it to a *height balanced BST*.

**Example**

Example 1:

```
	Input: array = 1->2->3
	Output:
		 2  
		/ \
		1  3
```

Example 2:

```
	Input: 2->3->6->7
	Output:
		 3
		/ \
	       2   6
		     \
		      7
```

**Explanation**

There may be multi answers, and you could return any of them.

```python
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """

    def sortedListToBST(self, head):
        # write your code here
        res = self.dfs(head)
        return res

    def dfs(self, head):
        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        dummy = ListNode(0)
        dummy.next = head
        fast = head
        slow = dummy

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        parent = TreeNode(temp.val)

        parent.left = self.dfs(head)
        parent.right = self.dfs(temp.next)

        return parent
```
