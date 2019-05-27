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