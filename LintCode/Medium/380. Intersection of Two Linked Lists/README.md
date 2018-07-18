# 380. Intersection of Two Linked Lists


- **Description**
    - Write a program to find the node at which the intersection of two singly linked lists begins.
    - If the two linked lists have no intersection at all, return **null**.
    - **The linked lists must retain their original structure after the function returns.**
    - You may assume there are no cycles anywhere in the entire linked structure.
- **Example**
    - The following two linked lists:

    ```
    A:          a1 → a2
                       ↘
                         c1 → c2 → c3
                       ↗            
    B:     b1 → b2 → b3
    ```

    - begin to intersect at node `c1`.
- **Challenge**
    - Your code should preferably run in `O(n)` time and use only `O(1)` memory.

    
## Solution

本题跟 **102. Linked List Cycle** 很类似，基本可以照搬解法，具体思路为：

- 不管有没有公共部分，把 `A` 的最后一个 `node` 连到 `B` 的头结点，创造一个环（如果有公共部分）或者仅仅是连在一起而已。
- 按照 `LinkedList Cycle` 快慢指针的做法 判断是否有环
- 若有环，继续判断第一个节点在哪里


### Code

```java
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
        // find last node of A, connect it to the head of B
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
        // use the two pointers to find it by moving at the same time
        // just remember using `slow.next` or will not AC
        ListNode start = headA;
        slow = slow.next;
        while (start != slow) {
            start = start.next;
            slow = slow.next;
        }
        
        // retain original structure
        pointer.next = null;
        return slow;
    }

}
```
