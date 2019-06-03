"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        if not A:
            return None
            
        nodes = [TreeNode(num) for num in A + [sys.maxsize]]
        stack = []
        for index, num in enumerate(A + [sys.maxsize]):
            while stack and A[stack[-1]] < num:
                top = stack.pop()
                left = A[stack[-1]] if stack else sys.maxsize
                if left < num:
                    nodes[stack[-1]].right = nodes[top]
                else:
                    nodes[index].left = nodes[top]
            
            stack.append(index)

        # sys.maxsize 's left child is the maximum number
        return nodes[-1].left
