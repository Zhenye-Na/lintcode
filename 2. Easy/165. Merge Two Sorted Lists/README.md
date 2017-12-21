# 165. Merge Two Sorted Lists

- **Description**
    - Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.
- **Example**
    - Given `1->3->8->11->15->null`, `2->null`, return `1->2->3->8->11->15->null`.

## Solution

Like **Merge Two Sorted Arrays**

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
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        result = dummy
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1         = l1.next
            else:
                dummy.next = l2
                l2         = l2.next

            dummy = dummy.next

        if l1:
            dummy.next = l1

        if l2:
            dummy.next = l2

        return result.next

```