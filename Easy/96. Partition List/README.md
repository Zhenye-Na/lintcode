# 96. Partition List

- **Description**
    - Given a linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`.
    - You should **preserve the original relative order of the nodes in each of the two partitions**.
- **Example**
    - Input: `head = 1->4->3->2->5->2`, `x = 3`
    - Output: `1->2->2->4->3->5`


## Solution

### Solution 1

从原LinkedList中删除小于x的元素，并放入一个新的 LinkedList，将新的与原来的链接在一起即可

- Time `O(n)`
- Space `O(k)` [k -> size(element < x)]


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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        newHead = ListNode(0)
        res = newHead

        curr = head
        prev = dummy

        while curr:
            if curr.val < x:

                # update left
                newHead.next = curr
                newHead = newHead.next

                # update pointers
                tmp = curr.next
                prev.next = tmp
                curr = tmp
            else:
                prev = curr
                curr = curr.next


        newHead.next = dummy.next
        return res.next
```

### Solution 2

分别new 两个 LinkedList 一个放比 `x` 小的，另一个放入大于等于 `x` 的, 然后连起来

- Time `O(n)`
- Space `O(n)`



```java
/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    public ListNode partition(ListNode head, int x) {
        if (head == null) {
            return null;
        }

        ListNode leftDummy  = new ListNode(0);
        ListNode rightDummy = new ListNode(0);
        ListNode left = leftDummy, right = rightDummy;

        while (head != null) {
            if (head.val < x) {
                left.next  = head;
                left       = head;
            } else {
                right.next = head;
                right      = head;
            }
            head = head.next;
        }

        right.next = null;
        left.next  = rightDummy.next;
        return leftDummy.next;
    }
}
```
