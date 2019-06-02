# 113. Remove Duplicates from Sorted List II

- **Description**
    - Given a sorted linked list, **delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.**
- **Example**
    - Given `1->2->3->3->4->4->5`, return `1->2->5`.
    - Given `1->1->1->2->3`, return `2->3`.

## Solution

###  Dummy Node + ListNode.next

```java
/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/


public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null)
            return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        head = dummy;

        while (head.next != null && head.next.next != null) {
            if (head.next.val == head.next.next.val) {
                int val = head.next.val;
                while (head.next != null && head.next.val == val) {
                    head.next = head.next.next;
                }
            } else {
                head = head.next;
            }
        }

        return dummy.next;
    }
}

```

### new LinkedList

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
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head:
            return head

        dummy = ListNode(0)
        newHead = dummy
        left  = head
        right = head.next

        while True:

            if not left:
                break

            # right points to None or left.val != right.val
            if not right or left.val != right.val:
                dummy.next = ListNode(left.val)
                dummy = dummy.next
                left  = left.next
                if right:
                    right = right.next
            else:
                # left.val == right.val
                val = right.val
                while right and val == right.val:
                    tmp = right
                    right = right.next

                left = tmp

                if left:
                    left   = left.next
                if right:
                    right  = right.next


        return newHead.next

```
