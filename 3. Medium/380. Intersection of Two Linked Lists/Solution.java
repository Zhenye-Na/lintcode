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
    /*
     * @param headA: the first list
     * @param headB: the second list
     * @return: a ListNode
     */
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // write your code here
        if (headA == null || headB == null) return null;
        
        ListNode result = findIntersection(headA, headB);
        return result;
    }
    

    private ListNode findIntersection(ListNode headA, ListNode headB) {
        // find lst node of A, connect it to the head of B
        ListNode pointer = headA;
        while(pointer.next != null) {
            pointer = pointer.next;
        }
        pointer.next = headB;
        
        // LinkedList cycle
        ListNode slow = headA;
        ListNode fast = headA.next;

        while (slow != fast) {
            if (fast.next != null && fast != null) {
                fast = fast.next.next;
                slow = slow.next;
            } else {
                return null;
            }
        }
        
        // find the node that intersection begins
        // let the two pointers find the starting nodes
        // just remember it
        ListNode start = headA;
        slow = slow.next;
        while (start != slow) {
            start = start.next;
            slow = slow.next;
        }
        pointer.next = null;
        return slow;
    }
    
    
}






/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

public class Solution {
    /**
     * @param headA: the first list
     * @param headB: the second list
     * @return: a ListNode 
     */
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }

        // get the tail of list A.
        ListNode node = headA;
        while (node.next != null) {
            node = node.next;
        }
        node.next = headB;
        ListNode result = listCycleII(headA);
        node.next = null;
        return result;
    }

    private ListNode listCycleII(ListNode head) {
        ListNode slow = head, fast = head.next;

        while (slow != fast) {
            if (fast == null || fast.next == null) {
                return null;
            }

            slow = slow.next;
            fast = fast.next.next;
        }

        slow = head;
        fast = fast.next;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }

        return slow;
    }
}