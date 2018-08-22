"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """
    def convertBST(self, root):
        # write your code here
        traverse = self.inorderTraversal(root)
        self.updateNode(traverse)
        return root

    def inorderTraversal(self, root):
        result = []
        if root is None:
            return result

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        result.extend(left)
        result.append(root)
        result.extend(right)

        return result

    def updateNode(self, traverse):
        left, right = len(traverse) - 2, len(traverse) - 1
        while left >= 0:
            traverse[left].val += traverse[right].val
            left  -= 1
            right -= 1





# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the new root
    def convertBST(self, root):
        # Write your code here
        self.sum = 0
        self.helper(root)
        return root

    def helper(self, root):
        if root is None:
            return
        if root.right:
            self.helper(root.right)

        self.sum += root.val
        root.val = self.sum
        if root.left:
            self.helper(root.left)
