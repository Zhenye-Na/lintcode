# 38. Search a 2D Matrix II

**Description**

Write an efficient algorithm that searches for a value in an `m x n` matrix, return the occurrence of it.

This matrix has the following properties:

- Integers in each row are sorted from left to right.
- Integers in each column are sorted from up to bottom.
- **No duplicate integers in each row or column.**

**Example**

```
Example 1:

Input:
	[[3,4]]
	target=3
Output:1
Example 2:

Input:
    [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
    target = 3
Output:2
```

**Challenge**

`O(m+n)` time and `O(1)` extra space



#### 遍历一下数组

#### 二维矩阵: 可以采用逼近法，从左下角开始往上逼近

<div>
  <img src="https://liweiwei1419.github.io/images/sword-for-offer/4-1.jpg" width="70%">
</div>

Assuming: No duplicate integers in each row or column 这一点很关键, 面试官可能不会给你这个方便 (?)

- 若等于 `target`, `count+=1`
- 若小于 `target`, 则这一列就可以划掉了（因为每一列的最下面一个数最大）
- 若大于 `target`, 则这一行就可以划掉了（因为每一行的最左边一个数最小）

#### 遍历 + 二分

从右上角到左下角遍历，时间复杂度O(m+n)，空间复杂度O(1)

遍历每行，在每行中用binary search，时间复杂度O(mlogn), 可以先对比行数和列数，然后遍历比较小的维度，二分搜索比较大的维度，时间复杂度 min ( O(mlogn), O(nlogm))

对比遍历和二分法，在行数列数接近的时候选用前者, 在 m >> n 或者 n >> m 的时候选择后者


```python
# 本参考程序来自九章算法，由 @Leon 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


def searchMatrix1(self,matrix,target):
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        if n == 0: return 0
        row,column = 0, n-1
        ans = 0
        while row < m and column >= 0:
            if matrix[row][column] < target:
                row += 1
            elif matrix[row][column] > target:
                column -= 1
            else:#matrix[row][colum] == target:
                ans += 1
                row += 1
        return ans
        
    def searchMatrix2(self, matrix, target):
        # write your code here
        def binarySearch(nums,target):
            left = 0
            right = len(nums)-1
            while left < right-1:
                mid = left + (right-left)/2
                if nums[mid] == target:
                    return 1
                elif nums[mid] < target:
                    left = mid
                else:
                    right = mid
            return 1 if nums[left] == target or nums[right] == target else 0
            
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        if n == 0: return 0
        ans = 0
        for i in range(m):
            ans += binarySearch(matrix[i],target)
        return ans
        
    def searchMatrix3(self, matrix, target):
        def searchRow(matrix,target):
            ans = 0
            for i in range(len(matrix)):
                left = 0
                right = len(matrix[i])-1
                while left < right-1:
                    mid = left + (right-left)/2
                    if matrix[i][mid] == target:
                        ans+=1
                        break # jump out of while loop
                    elif matrix[i][mid] < target:
                        left = mid
                    else:
                        right = mid
                if matrix[i][left] == target or matrix[i][right] == target:
                    ans += 1
            return ans
        
        def searchColumn(matrix,target):
            ans = 0
            for i in range(len(matrix[0])):
                left = 0
                right = len(matrix)-1
                while left < right-1:
                    mid = left + (right-left)/2
                    if matrix[mid][i] == target:
                        ans+=1
                        break # jump out of while loop
                    elif matrix[mid][i] < target:
                        left = mid
                    else:
                        right = mid
                if matrix[left][i] == target or matrix[right][i] == target:
                    ans += 1
            return ans
        
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        if n == 0: return 0
        if m < n:
            return searchRow(matrix,target)
        else:
            return searchColumn(matrix,target)
```
