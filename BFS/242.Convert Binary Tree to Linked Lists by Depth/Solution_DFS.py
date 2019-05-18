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
        result = []
        self.dfs(root, 1, result)
        return result

    def dfs(self, root, depth, result):
        if root is None:
            return

        node = ListNode(root.val)
        if len(result) < depth:
            result.append(node)
        else:
            node.next = result[depth - 1]
            result[depth - 1] = node
        
        self.dfs(root.right, depth + 1, result)
        self.dfs(root.left, depth + 1, result)