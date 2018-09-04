# 103. Linked List Cycle II

- **Description**
    - Given a linked list, return the node where the cycle begins.
    - If there is no cycle, return null.
- **Example**
    - Given `-21->10->4->5`, tail connects to node index `1`
    - return `10`
- **Challenge**
    - Follow up:
        - Can you solve it without using extra space?

## Solution

详细思路参考 [Linked List Cycle & Linked List Cycle II 单链表中的环](https://zhenye-na.github.io/2018/09/03/linkedlist-cycle-ii.html)

> For the reason why we can solve this problem with two pointers, you can refer to [this](https://www.cnblogs.com/hiddenfox/p/3408931.html) blog post


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
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if not head or not head.next:
            return None

        # Two Pointers -> test whether there is cycle in the LinkedList
        slow, fast = head, head.next
        while slow != fast:
            if fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None

        # Find the first node in the circle
        pointer = head
        while pointer != slow.next:
            slow = slow.next
            pointer = pointer.next

        return pointer
```
