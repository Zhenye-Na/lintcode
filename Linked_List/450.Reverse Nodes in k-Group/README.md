# 450. Reverse Nodes in k-Group

**Description**

Given a linked list, reverse the nodes of a linked list `k` at a time and return its modified list.

If the number of nodes is not a multiple of `k` then left-out nodes in the end should remain as it is.

```
You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.
```

**Example**

Example 1

```
Input:
list = 1->2->3->4->5->null
k = 2
Output:
2->1->4->3->5
```

Example 2

```
Input:
list = 1->2->3->4->5->null
k = 3
Output:
3->2->1->4->5
```

需要"分段"进行 reverse，如果最后 nodes 不足 `k` 个，那么不进行 reverse。用到了 **dummy node**， 最后结果 `return dummy.next`. **36. Reverse Linked List II** 的变体


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
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        if not head:
            return head

        dummy = ListNode(0, head)
        head = dummy

        while head:
            head = self._reverseK(head, k)

        return dummy.next

    def _reverseK(self, node, k):
        n1, nk = node.next, node
        for _ in range(k):
            nk = nk.next
            if nk is None:
                return nk

        nk_next = nk.next

        # reverse
        prev, curt = None, n1
        while curt != nk_next:
            tmp = curt.next
            curt.next = prev
            prev = curt
            curt = tmp

        # connect
        node.next = nk
        n1.next = nk_next

        return n1

```