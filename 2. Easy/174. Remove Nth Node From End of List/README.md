# 174. Remove Nth Node From End of List

Description
Given a linked list, remove the nth node from the end of list and return its head.

The minimum number of nodes in list is n.

Have you met this question in a real interview?  
Example
Given linked list: 1->2->3->4->5->null, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5->null.

Challenge
Can you do it without getting the length of the linked list?

## Solution

### Length of Linked List is known

头指针可能改变， 所以要用dummy node, return dummy.next


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
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        keep = length - n
        curr = head
        i = 1
        while i <= keep and curr:
            prev = curr
            curr = curr.next
            i += 1

        prev.next = curr.next
        return dummy.next
```


### Length of Linked List is unknown

```python
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution(object):
    '''
    题意：删除链表中倒数第n个结点，尽量只扫描一遍。
    使用两个指针扫描，当第一个指针扫描到第N个结点后，
    第二个指针从表头与第一个指针同时向后移动，
    当第一个指针指向空节点时，另一个指针就指向倒数第n个结点了       
    '''
    def removeNthFromEnd(self, head, n):
        res = ListNode(0)
        res.next = head
        tmp = res

        for i in range(0, n):
            head = head.next

        while head != None:
            head = head.next
            tmp = tmp.next

        tmp.next = tmp.next.next
        return res.next
```
