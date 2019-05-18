from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        nodeList = []
        if root is None:
            return nodeList

        queue = deque([])
        queue.append(root)

        while queue:
            first = ListNode(0)
            dummy = first
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                newlistNode = ListNode(node.val)
                first.next = newlistNode
                first = newlistNode

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            nodeList.append(dummy.next)

        return nodeList
