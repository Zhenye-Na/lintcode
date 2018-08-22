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
