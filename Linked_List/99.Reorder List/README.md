# 99. Reorder List

**Description**

Given a singly linked list `L: L0 -> L1 -> ... -> Ln-1 -> Ln`

reorder it to: `L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...`

**Example**


Example 1:

```
Input:  1->2->3->4->null
Output: 1->4->2->3->null
```

Example 2:

```
Input: 1->2->3->4->5->null
Output: 1->5->2->4->3->null
```


快慢指针找到中点, 将右半段逆序, 然后 merge list

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
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if not head:
            return head

        # 1. Find middle ListNode
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow == fast:
            return head

        second_head = slow.next
        slow.next = None

        prev, curt = None, second_head
        while curt:
            tmp = curt.next
            curt.next = prev
            prev = curt
            curt = tmp

        # 2. Reverse sencond half of LinkedList
        p1, p2 = head, prev
        dummy = ListNode(0)
        head = dummy
        length = 1
        while p1 and p2:
            if length % 2 == 1:
                head.next = p1
                p1 = p1.next
                length += 1
            else:
                head.next = p2
                p2 = p2.next
                length += 1
            head = head.next

        if p1:
            head.next = p1
        else:
            head.next = p2

        return dummy.next
```
