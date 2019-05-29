# 372. Delete Node in a Linked List

**Description**

Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

**Example**

Example 1:

```
Input:
1->2->3->4->null
3
Output:
1->2->4->null
```

Example 2:

```
Input:
1->3->5->null
3
Output:
1->5->null
```


```python
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    def deleteNode(self, node):
        # write your code here
        if not node or not node.next:
            node = None
            return

        node.val = node.next.val
        node.next = node.next.next
```