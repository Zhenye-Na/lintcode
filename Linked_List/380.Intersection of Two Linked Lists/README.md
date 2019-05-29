# 380. Intersection of Two Linked Lists

**Description**

Write a program to find the node at which the intersection of two singly linked lists begins.

```
1. If the two linked lists have no intersection at all, return null.
2. The linked lists must retain their original structure after the function returns.
3. You may assume there are no cycles anywhere in the entire linked structure.
```

**Example**

Example 1:

```
Input:
	A:          a1 → a2
	                   ↘
	                     c1 → c2 → c3
	                   ↗            
	B:     b1 → b2 → b3
Output: c1
Explanation: begin to intersect at node c1.
```

Example 2:

```
Input:
Intersected at 6
1->2->3->4->5->6->7->8->9->10->11->12->13->null
6->7->8->9->10->11->12->13->null
Output: Intersected at 6
Explanation: begin to intersect at node 6.
```

**Challenge**

Your code should preferably run in `O(n)` time and use only `O(1)` memory.

**Linked List Cycle II 变种**


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
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if not headA or not headB:
            return None

        # Find last ListNode
        a = headA
        while a.next:
            a = a.next

        a.next = headB

        # Fast - Slow pointers
        haveIntersection = False
        slow, fast = headA, headA
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                haveIntersection = True
                break

        if haveIntersection:
            third = headA
            while third != slow:
                third = third.next
                slow = slow.next
            return slow

        return None
```