"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        # write your code here
        if not l1 and not l2:
            return None

        if not l1 and l2:
            return self.list2num(l2)

        if not l2 and l1:
            return self.list2num(l1)

        num1 = self.list2num(l1)
        num2 = self.list2num(l2)

        l3 = self.num2list(num1 + num2)

        return l3


    def num2list(self, num):
        """
        transform number to LinkedList
        @param num: the number needed to be transformed
        """
        if num == 0:
            return ListNode(0)

        q = []
        while num != 0:
            q.append(num % 10)
            num = num / 10

        node = ListNode(q.pop(0))
        dummy = node
        while q:
            node.next = ListNode(q.pop(0))
            node = node.next

        return dummy

    def list2num(self, l):
        """
        transform LinkedList to number
        @param l: the LinkedList needed to be transformed
        """

        stack = []
        head  = l

        while head:
            stack.append(head.val)
            head = head.next

        num = 0
        while stack:
            num = num * 10 + stack.pop()

        return num
