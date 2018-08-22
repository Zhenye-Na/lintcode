# 372. Delete Node in a Linked List

- **Description**
    - Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.
- **Example**
    - Linked list is `1->2->3->4`, and given node `3`, delete the node in place `1->2->4`

## Solution

这道题让我们删除链表的一个节点，更通常不同的是，没有给我们链表的起点，只给我们了一个要删的节点，跟我们以前遇到的情况不太一样，我们之前要删除一个节点的方法是要有其前一个节点的位置，然后将其前一个节点的next连向要删节点的下一个，然后delete掉要删的节点即可。这道题的处理方法是先把当前节点的值用下一个节点的值覆盖了，然后我们删除下一个节点即可


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
     * @param node: the node in the list should be deleted
     * @return: nothing
     */
    public void deleteNode(ListNode node) {
        // write your code here
        if (node == null || node.next == null) return;
        
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
```