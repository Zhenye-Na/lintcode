# 35. Reverse Linked List

- **Description**
    - Reverse a linked list.  
- **Example**
    - For linked list `1->2->3->null`, the reversed linked list is `3->2->1->null`
- **Challenge**
    - Reverse it in-place and in one-pass


## Solution

记住这四行即可：

```java
ListNode tmp = head.next;
head.next = prev;
prev = head;
head = tmp;
```


### Code

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