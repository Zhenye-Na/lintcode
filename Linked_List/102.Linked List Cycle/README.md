# 102. Linked List Cycle

**Description**

Given a linked list, determine if it has a cycle in it.

**Example**

```
Example 1:
    Input: 21->10->4->5,  then tail connects to node index 1(value 10).
    Output: true
    
Example 2:
    Input: 21->10->4->5->null
    Output: false
```

**Challenge**

Follow up: Can you solve it without using extra space?



这道题解法比较有趣，**"两根指针"**

一个跑得快，一个跑得慢，如果有 `cycle` 存在，那么迟早这两根指针会指向同一个 `ListNode`，而如果 `fast` 跑完了也没遇上 `slow`，那么就不存在 `cycle`



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
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if not head:
            return False

        slow, fast = head, head.next

        while slow != fast:
            # fast pointer is None -> no cycle
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        # If slow and fast pointers point to the same element after loop -> cycle exists
        return True
```
