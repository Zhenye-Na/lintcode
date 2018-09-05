class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        # write your code here
        if n <= 0:
            return 1

        # Table to store results of subproblems
        catalan = [0 for i in range(n + 1)]

        # Initialize first two values in table
        catalan[0] = 1
        catalan[1] = 1

        # Fill entries in catalan[] using recursive formula
        for i in range(2, n + 1):
            catalan[i] = 0
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]

        # Return last entry
        return catalan[n]



# 一棵树由根节点，左子树和右子树构成。
# 对于目标n，根节点可以是1, 2, ..., n中的任意一个，假设根节点为k，
# 那么左子树的可能性就是numTrees(k-1)种，右子树的可能性就是numTrees(n-k)种，
# 他们的乘积就根节点为k时整个树的可能性。把所有k的可能性累加就是最终结果。

# 本参考程序来自九章算法，由 @Q同学 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        ans = {0: 1,
               1: 1,
               2: 2}
        return self.helper(n, ans)

    def helper(self, n, ans):
        if n in ans:
            return ans[n]
        else:
            # for each root node, there are
            # (numTrees(left_subtree)) * (numTrees(right_subtree)) unique BST's
            res = 0
            for i in range(n):
                res += self.helper(i, ans) * self.helper(n - i - 1, ans)
            ans[n] = res
            return res
