# 170. Rotate List

**Description**

Given a list, rotate the list to the right by k places, where k is non-negative.

**Example**

Example 1:

```
Input:1->2->3->4->5  k = 2
Output:4->5->1->2->3
```

Example 2:

```
Input:3->2->1  k = 1
Output:1->3->2
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
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        if not head or k < 0:
            return head

        node, size = head, 1
        while node:
            node = node.next
            size += 1

        size -= 1
        k = k % size

        if k == 0:
            return head

        node = head
        for _ in range(size - k - 1):
            node = node.next

        new_end, new_head = node, node.next
        pointer = new_head
        while pointer.next:
            pointer = pointer.next

        pointer.next = head
        new_end.next = None

        return new_head
```
