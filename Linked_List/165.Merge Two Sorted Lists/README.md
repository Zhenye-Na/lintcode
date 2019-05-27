# 165. Merge Two Sorted Lists

**Description**

Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.

**Example**

```
Example 1:
	Input: list1 = null, list2 = 0->3->3->null
	Output: 0->3->3->null


Example 2:
	Input:  list1 =  1->3->8->11->15->null, list2 = 2->null
	Output: 1->2->3->8->11->15->null
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
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        p1, p2 = l1, l2
        dummy = ListNode(0)

        head = dummy
        while p1 and p2:
            if p1.val < p2.val:
                head.next = p1
                p1 = p1.next
            else:
                head.next = p2
                p2 = p2.next
            head = head.next

        if p1:
            head.next = p1

        if p2:
            head.next = p2


        return dummy.next
```
