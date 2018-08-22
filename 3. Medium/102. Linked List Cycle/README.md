# 102. Linked List Cycle


- **Description**
    - Given a linked list, determine if it has a **cycle** in it.
- **Example**
    - Given `-21->10->4->5`, tail connects to node index `1`, return true
- **Challenge**
    - Follow up:
        - Can you solve it without using extra space?



## Solution

这道题解法比较有趣，**“两根指针”**

一个跑得快，一个跑得慢，如果有 `cycle` 存在，那么迟早这两根指针会指向同一个 `ListNode`，而如果 `fast` 跑完了也没遇上 `slow`，那么就不存在 `cycle`



```java
/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */


public class Solution {
    /*
     * @param head: The first node of linked list.
     * @return: True if it has a cycle, or false
     */
    public boolean hasCycle(ListNode head) {
        // write your code here
        if (head == null || head.next == null) return false;
        
        ListNode slow = head;
        ListNode fast = head.next;
        
        while (fast != slow) {
            if (fast.next == null || fast.next.next == null) {
                return false;
            }
            
            fast = fast.next.next;
            slow = slow.next;
        }

        return true;
    }
}
```