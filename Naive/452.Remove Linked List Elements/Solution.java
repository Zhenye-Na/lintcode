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
     * @param val: An integer
     * @return: a ListNode
     */
    public ListNode removeElements(ListNode head, int val) {
        // write your code here

        // if head is null, return
        if (head == null) return null;

        ListNode p = head;
        ListNode q = head.next;

        // skip the the value which equals to `val`
        while(q!= null) {
            if (q.val == val) {
                p.next = q.next;
                q = q.next;
            } else {
                p = p.next;
                q = q.next;
            }
        }

        // check the first item
        if (head.val == val) return head.next;
        return head;
    }
}