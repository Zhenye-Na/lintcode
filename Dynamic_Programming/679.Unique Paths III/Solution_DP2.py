# 本参考程序来自九章算法，由 @Bobby 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    def uniqueWeightedPaths(self, grid):
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        tmp, sumset = 0, []
        for v in grid[0]:
            tmp += v
            sumset.append({tmp})
        
        for i in range(1,n):
            for j in range(m):
                if j == 0:
                    v = sumset[j].pop() + grid[i][j]
                    sumset[j] = {v}
                else:
                    sumset[j] = {grid[i][j] + v for v in sumset[j].union(sumset[j-1])}
        return sum(sumset[m-1])