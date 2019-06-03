# 1292. Odd Even Linked List

**Description**

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

```
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
```

**Example**

Example 1:

```
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
```

Example 2:

```
Input: 2->1->null
Output: 2->1->null
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
    @param head: a singly linked list
    @return: Modified linked list
    """
    def oddEvenList(self, head):
        # write your code here
        if not head:
            return head

        odd = head
        even = head.next

        o, e = odd, even
        while e and e.next:
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next

        o.next = even
        return head
```