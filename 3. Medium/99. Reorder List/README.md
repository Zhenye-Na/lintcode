# 99. Reorder List

- **Description**
    - Given a singly linked list L: `L0 → L1 → ... → Ln-1 → Ln`
    - reorder it to: `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`
- **Example**
    - Given `1->2->3->4->null`, reorder it to `1->4->2->3->null`.
- **Challenge**
    - Can you do this in-place without altering the nodes' values?

## Solution

### `O(1)` Space

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
    def findMiddle(self, h):
        slow, fast = h, h.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def reverse(self, h):
        prev = None
        while h:
            tmp    = h.next
            h.next = prev
            prev   = h
            h      = tmp
        return prev


    def reorderList(self, head):
        if head is None or head.next is None:
            return head
        mid      = self.findMiddle(head)
        last     = self.reverse(mid.next)
        mid.next = None

        while last:
            tmp       = head.next
            head.next = last
            h         = last.next

            last.next = tmp
            head      = tmp
            last      = h
```


### `O(n)` Space + Alter values

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
        if not head or not head.next:
            return head

        nums = []
        pointer = head
        while pointer:
            nums.append(pointer.val)
            pointer = pointer.next

        left, right = 0, len(nums) - 1
        dummy = head
        flag = True

        while left <= right:
            if flag:
                dummy.val = nums[left]
                left += 1
            else:
                dummy.val = nums[right]
                right -= 1
            dummy  = dummy.next
            flag = not flag

        return head
```

### `O(n)` Space + Dictionay

```python
# pass
```
