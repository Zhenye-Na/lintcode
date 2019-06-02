# 112. Remove Duplicates from Sorted List

- **Description**
    - Given a sorted linked list, delete all duplicates such that each element appear only once.
- **Example**
    - Given `1->1->2`, return `1->2`.
    - Given `1->1->2->3->3`, return `1->2->3`.


## Solution

### Two Pointers

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
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head:
            return head
        prev = head
        curr = head
        result = head
        while curr:
            if curr.val != prev.val:
                prev.next.val = curr.val
                prev = prev.next
            curr = curr.next

        prev.next = None
        return result
```

### One pointer


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
        if (head == null) {
            return null;
        }

        ListNode node = head;
        while (node.next != null) {
            if (node.val == node.next.val) {
                node.next = node.next.next;
            } else {
                node = node.next;
            }
        }
        return head;
    }
}
```
