# 本参考程序来自九章算法，由 @This is Anfield 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param: root: param root: The root of the binary search tree
    @param: k1: An integer
    @param: k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        ret = []
        self.search(root, k1, k2, ret)
        return ret

    def search(self, root, k1, k2, ret):
        if root == None:
            return
        if root.val > k2:
            self.search(root.left, k1, k2, ret)
        elif root.val < k1:
            self.search(root.right, k1, k2, ret)
        else:
            self.search(root.left, k1, k2, ret)
            ret.append(root.val)
            self.search(root.right, k1, k2, ret)






# 本参考程序来自九章算法，由 @蒋同学 提供。版权所有，转发请注明出处。
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
from collections import deque
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        if not root:
            return []
        result = []
        queue  = deque([root])

        while queue:
            node = queue.popleft()
            if k1 <= node.val and node.val <= k2:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result







"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        result = []
        if not root:
            return result
        nums = self.inorderTraverse(root)

        if len(nums) == 1:
            if nums[0] >= k1 and nums[0] <= k2:
                return nums
            else:
                return result

        idx1 = self.binarySearch(nums, k1, True)
        idx2 = self.binarySearch(nums, k2, False)
        if idx1 == -1 and idx2 == -1:
            return result
        if idx1 == -1:
            idx1 = 0
        if idx2 == -1:
            idx2 = len(nums)

        return nums[idx1: idx2 + 1]


    def inorderTraverse(self, root):
        result = []
        if not root:
            return result

        left  = self.inorderTraverse(root.left)
        right = self.inorderTraverse(root.right)

        result.extend(left)
        result.append(root.val)
        result.extend(right)

        return result


    def binarySearch(self, nums, target, flag):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (end - start) / 2 + start

            if target == nums[mid]:
                if flag:
                    end = mid
                else:
                    start = mid
            elif target > nums[mid]:
                start = mid
            else:
                end = mid

        if flag:
            if target <= nums[start]:
                return start
            if target <= nums[end]:
                return end
        else:
            if target >= nums[end]:
                return end
            if target >= nums[start]:
                return start
        return -1
