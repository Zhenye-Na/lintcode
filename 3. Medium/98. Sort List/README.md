# 98. Sort List

- **Description**
    - Sort a linked list in `O(n logn)` time using constant space complexity.
- **Example**
    - Given `1->3->2->null`, sort it to `1->2->3->null`.
- **Challenge**
    - Solve it by merge sort & quick sort separately.


## Solution

这答案我没话说，背吧

### Merge Sort

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
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        def merge(list1, list2):
            if list1 == None:
                return list2
            if list2 == None:
                return list1

            head = None

            if list1.val < list2.val:
                head  = list1
                list1 = list1.next
            else:
                head  = list2;
                list2 = list2.next;

            tmp = head

            while list1 != None and list2 != None:
                if list1.val < list2.val:
                    tmp.next = list1
                    tmp      = list1
                    list1    = list1.next
                else:
                    tmp.next = list2
                    tmp      = list2
                    list2    = list2.next

            if list1 != None:
                tmp.next = list1;
            if list2 != None:
                tmp.next = list2;

            return head;

        # start here
        if head == None:
            return head
        if head.next == None:
            return head

        fast = head
        slow = head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        list1  = self.sortList(head)
        list2  = self.sortList(mid)

        sorted = merge(list1,list2)

        return sorted
```

自己默写的版本


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
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        def merge(l1, l2):
            if not l1:
                return l2

            if not l2:
                return l1

            head = None

            if l1.val < l2.val:
                head = l1
                l1   = l1.next
            else:
                head = l2
                l2   = l2.next

            dummy = head

            while l1 and l2:
                if l1.val < l2.val:
                    head.next = l1
                    head      = l1
                    l1        = l1.next
                else:
                    head.next = l2
                    head      = l2
                    l2        = l2.next

            if l1:
                head.next = l1
            if l2:
                head.next = l2

            return dummy




        if not head or not head.next:
            return head

        # Find mid position of LinkedList
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # When exit slow point to the "mid" position
        # of the LinkedList
        # So, we split it into to parts
        right     = slow.next
        slow.next = None

        # Divide
        l1 = self.sortList(head)
        l2 = self.sortList(right)

        # Merge
        newHead = merge(l1, l2)
        return newHead
```



### [Failed] LinkedList -> Array -> Quick Sort

说一下自己的思路吧，反正 Failed 了

- 思路1: 创建一个新的 Class DoublyLinkedList()， 然后用 Quick Sort 思想去做 [Failed]
- 思路2: 从 LinkedList -> Array -> Quick Sort -> LinkedList [Failed]


```python
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
```
