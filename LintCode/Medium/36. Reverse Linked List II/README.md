# 36. Reverse Linked List II


- **Description**
    - Reverse a linked list from position m to n.
    - Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list. 
- **Example**
    - Given `1->2->3->4->5->NULL`, `m = 2` and `n = 4`, return `1->4->3->2->5->NULL`.
- **Challenge**
    - Reverse it in-place and in one-pass


## Solution

一道和 **dummy node** 有关的题目，要求把 [m,n] 之间的 nodes reverse，但是其实一共有 `(m-n+1)` 个点的 next 发生了变化。注意 reverse 结束后将 LinkedList 重新拼好。


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
     * @param head: ListNode head is the head of the linked list 
     * @param m: An integer
     * @param n: An integer
     * @return: The head of the reversed ListNode
     */
    public ListNode reverseBetween(ListNode head, int m, int n) {
        // write your code here
        if (m >= n || head == null) {
            return head;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        head = dummy;
        
        for (int i = 1; i < m; i++) {
            if (head == null) {
                return null;
            }
            head = head.next;
        }
        
        ListNode premNode = head;
        ListNode mNode = head.next;
        ListNode nNode = mNode, postnNode = mNode.next;

        for (int i = m; i < n; i++) {
            if (postnNode == null) {
                return null;
            }
            ListNode temp = postnNode.next;
            postnNode.next = nNode;
            nNode = postnNode;
            postnNode = temp;
        }

        mNode.next = postnNode;
        premNode.next = nNode;
        
        return dummy.next;
    }
}
```