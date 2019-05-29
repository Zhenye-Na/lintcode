"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    def deleteNode(self, node):
        # write your code here
        if not node or not node.next:
            node = None
            return

        node.val = node.next.val
        node.next = node.next.next