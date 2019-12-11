# 96. Partition List

**Description**

Given a linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`.

```
You should preserve the original relative order of the nodes in each of the two partitions.
```

**Example**

Example 1:

```
Input: list = null, x = 0
Output: null	
Explanation: The empty list Satisfy the conditions by itself.
```

Example 2:

```
Input: list = 1->4->3->2->5->2->null, x = 3
Output: 1->2->2->4->3->5->null	
Explanation: Keep the original relative order of the nodes in each of the two partitions.
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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        # write your code here
        if head is None:
            return head

        aHead, bHead = ListNode(0), ListNode(0)
        aTail, bTail = aHead, bHead

        while head is not None:
            if head.val < x:
                aTail.next = head
                aTail = aTail.next
            else:
                bTail.next = head
                bTail = bTail.next
            head = head.next

        bTail.next = None
        aTail.next = bHead.next
        return aHead.next
```