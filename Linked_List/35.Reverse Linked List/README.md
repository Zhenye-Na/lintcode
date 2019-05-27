# 35. Reverse Linked List

**Description**

Reverse a linked list.  

**Example**

Example 1:

```
Input: 1->2->3->null
Output: 3->2->1->null
```

Example 2:

```
Input: 1->2->3->4->null
Output: 4->3->2->1->null
```

**Challenge**

Reverse it in-place and in one-pass.


## Solution

记住这四行即可：

```java
ListNode tmp = head.next;
head.next    = prev;
prev         = head;
head         = tmp;
```

### Python

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
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        prev = None
        while head:
            # mark next list node
            tmp = head.next

            # swap order
            head.next = prev

            # update pointers
            prev = head
            head = tmp

        return prev

```


### Java

```java
/**
 * Definition for ListNode
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
    /**
     * @param head: n
     * @return: The new head of reversed linked list.
     */
    public ListNode reverse(ListNode head) {
        // write your code here
        ListNode prev = null;

        while (head != null) {
            ListNode tmp = head.next;
            head.next = prev;
            prev = head;
            head = tmp;
        }

        return prev;
    }
}
```
