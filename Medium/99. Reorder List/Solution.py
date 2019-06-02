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
            # Connect from left to right
            tmp       = head.next
            head.next = last

            # Connect from right to left
            h         = last.next
            last.next = tmp

            # Update pointers
            head      = tmp
            last      = h




# O(n) Space

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
