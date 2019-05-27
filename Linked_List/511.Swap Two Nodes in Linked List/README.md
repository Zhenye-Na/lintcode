# 511. Swap Two Nodes in Linked List

**Description**

Given a linked list and two values `v1` and `v2`. Swap the two nodes in the linked list with values `v1` and `v2`. It's guaranteed there is no duplicate values in the linked list. If `v1` or `v2` does not exist in the given linked list, do nothing.

```
You should swap the two nodes with values `v1` and `v2`. Do not directly swap the values of the two nodes.
```

**Example**
Example 1:

Input: 1->2->3->4->null, v1 = 2, v2 = 4
Output: 1->4->3->2->null
Example 2:

Input: 1->null, v1 = 2, v2 = 1
Output: 1->null


因为数据结构是单链表, 所以假设需要修改权值为 v 的节点的链接, 那么需要获取该节点的前驱节点.

我们需要定义一个虚节点, 作为链表头, 它不储存数据.

找到权值为 `v1` 和 `v2` 的节点之后, 分情况讨论:

- 如果二者本身是**相邻**的, 则一共需要修改三条边 (即三个next关系) `{a node} -> {v = v1} -> {v = v2} -> {a node}`
- 如果二者是**不相邻**的, 则一共需要修改四条边 `{a node} -> {v = v1} -> {some nodes} -> {v = v2} -> {a node}`

假定 `v1` 在 `v2` 前

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
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        if not head:
            return head

        dummy = ListNode(0, head)

        n1, n2 = None, None
        n1_prev, n2_prev = None, None
        prev = dummy
        node = dummy.next

        while node:
            if node.val == v1:
                n1 = node
                n1_prev= prev
            if node.val == v2:
                n2 = node
                n2_prev = prev
            prev = node
            node = node.next

        if n1 is None or n2 is None:
            return dummy.next

        n1_next = n1.next
        n2_next = n2.next

        # swap
        if n1.next == n2:
            n1_prev.next = n2
            n2.next = n1
            n1.next = n2_next
        
        elif n2.next == n1:
            n2_prev.next = n1
            n1.next = n2
            n2.next = n1_next

        else:
            n1_prev.next = n2
            n2.next = n1_next
            n2_prev.next = n1
            n1.next = n2_next

        return dummy.next
```