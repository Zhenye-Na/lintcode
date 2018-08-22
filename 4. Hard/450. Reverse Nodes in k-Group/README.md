# 450. Reverse Nodes in k-Group

- **Description**
    - Given a linked list, reverse the nodes of a linked list `k` at a time and return its modified list.
    - **If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.**
    - You may not alter the values in the nodes, only nodes itself may be changed.
    - **Only constant memory is allowed.**
- **Example**
    - Given this linked list: `1->2->3->4->5`
    - For `k = 2`, you should return: `2->1->4->3->5`
    - For `k = 3`, you should return: `3->2->1->4->5`


## Solution

**36. Reverse Linked List II** 的变体

需要“分段”进行 reverse，如果最后nodes不足 k 个，那么不进行 reverse。
用到了 **dummy node**， 最后结果 `return dummy.next`


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
     * @param head: a ListNode
     * @param k: An integer
     * @return: a ListNode
     */
    public ListNode reverseKGroup(ListNode head, int k) {
        // write your code here
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        head = dummy;
        
        while (head != null) {
            head = reverseKNodes(head, k);
        }
        return dummy.next;
    }
    
    private ListNode reverseKNodes(ListNode head, int k) {
        
        // head -> n1 -> n2 -> n3 -> ... -> nk -> nk+1
        // head -> nk -> ... -> n1 -> nk+1
        // reverse from n1 ~ nk
        // return n1
        ListNode first = head.next;
        ListNode counter = head;
        for (int i = 0; i < k; i++) {
            counter = counter.next;
            if (counter == null) {
                return null;
            }
        }
        
        // counter => last node to reverse in this batch
        
        ListNode nextNode = counter.next;
        ListNode prev = null;
        ListNode curr = first;
        while (curr != nextNode) {
            ListNode tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }
        
        first.next = nextNode;
        head.next = counter;
        
        return first;
    }

}
```