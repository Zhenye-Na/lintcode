"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        return self._dfs(head)


    def _dfs(self, head):
        if not head:
            return head

        if head.next is None:
            return TreeNode(head.val)

        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tmp = slow.next
        slow.next = None

        root = TreeNode(tmp.val)
        root.left = self._dfs(head)
        root.right = self._dfs(tmp.next)

        return root
