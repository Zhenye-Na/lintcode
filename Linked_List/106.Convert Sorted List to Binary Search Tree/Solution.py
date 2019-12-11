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
        res = self.dfs(head)
        return res

    def dfs(self, head):
        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        dummy = ListNode(0)
        dummy.next = head
        fast = head
        slow = dummy

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        parent = TreeNode(temp.val)

        parent.left = self.dfs(head)
        parent.right = self.dfs(temp.next)

        return parent
