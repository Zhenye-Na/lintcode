# 106. Convert Sorted List to Binary Search Tree

- **Description**
    - Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
- **Example**

    ```
                   2
    1->2->3  =>   / \
                 1   3
    ```


## Solution

### Recursion

做过Ladder前面几道题就基本知道这道题怎么做了

- 首先找到 mid (两根指针)，让 mid 做 root，然后 split LinkedList
- Recursion 左边的 Linked List，让中间的做 root.left; Recursion 右边的 Linked List，让中间的做 root.right


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

        # base case
        if not head:
            return head

        if not head.next:
            return TreeNode(head.val)

        # find middle position of current Linked List
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # create TreeNode
        mid       = slow.next
        slow.next = None
        root      = TreeNode(mid.val)

        # recursive case
        root.left  = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root
```
