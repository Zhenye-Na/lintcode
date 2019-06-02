"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import random

class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not head or not head.next:
            return head

        nums = self.list2array(head)
        self.quickSort(nums, 0, len(nums)-1)
        return self.array2list(nums)



    def list2array(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums


    def quickSort(self, A, start, end):
        # base case
        if start >= end:
            return

        pivotIndex = random.randint(start, end)
        pivot      = A[pivotIndex]

        left, right = start, end

        while left <= right:

            while left <= right and A[left] < pivot:
                left += 1

            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]

                left  += 1
                right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)



    def array2list(self, nums):
        dummy = ListNode(0)
        head = dummy
        for num in nums:
            head.next = ListNode(num)
            head.next = head
        return dummy.next
