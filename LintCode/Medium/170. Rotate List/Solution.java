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
     * @param head: the List
     * @param k: rotate to the right k places
     * @return: the list after rotation
     */
    public ListNode rotateRight(ListNode head, int k) {
        // write your code here
        if (k < 0 || head == null) return head;

        // get the length of list
        int size = 0;
        ListNode curr = head;
        while (curr != null) {
            size++;
            curr = curr.next;
        }

        k = k % size;
        if (size == 1 || k == 0) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;


        ListNode first = dummy;
        for (int i = 0; i < size - k; i++) {
            first = first.next;
        }

        ListNode newHead = first.next;
        first.next = null;

        ListNode tail = newHead;
        while (tail.next != null) {
            tail = tail.next;
        }

        tail.next = dummy.next;

        return newHead;
    }
}
