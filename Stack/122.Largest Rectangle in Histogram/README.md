# 122. Largest Rectangle in Histogram

**Description**

Given `n` non-negative integers representing the histogram's bar height where the width of each bar is `1`, find the area of largest rectangle in the histogram.


**Example**

Example 1:

```
Input: [2,1,5,6,2,3]
Output: 10
Explanation:
The third and fourth rectangular truncated rectangle has an area of 2 * 5 = 10.
```

Example 2:

```
Input: [1,1]
Output: 2
Explanation:
The first and second rectangular truncated rectangle has an area of 2 * 1 = 2.
```


**单调栈解法**

*O(n)*

每个元素进栈出栈 -> O(n)

*讲解:*

- 柱子下标是 `i` 和 `j`, 同时 `i < j`, `A[i] >= A[j]`, 那么下标为 `i` 的柱子一定不会是后面某根柱子的下边界. 那么 `A[i]` 就可以从候选列表里删掉, 维护一个**单调递增栈**
- 下面代码中, `h = height[stack.pop()]` 可以知道左边界和右边界, 因为是 `cur` 这根柱子让 `h` 从栈中 `pop` 出来, (假如 `cur` 不是他的右边界, 那么 `h` 早就 `pop` 出来了), 左边界就是现在的**栈顶元素**
- 以 h 为高度的矩形, 被 cur 以右边界限制住了, 即使 cur 右边有比 cur 还矮的柱子, 以 h 为高的矩形也画不过去
- `cur = -1` 这一步操作是为了清空栈

```python
class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if not height or len(height) == 0:
            return 0

        area = 0
        stack = []
        for i in range(len(height) + 1):
            cur = -1 if i == len(height) else height[i]
            while stack and height[stack[-1]] >= cur:
                h = height[stack.pop()]
                w = i if len(stack) == 0 else i - stack[-1] - 1
                area = max(area, h * w)

            stack.append(i)

        return area
```


**O(n^2) 解法**

两根指针, for 循环每一根柱子, 去找到比当前循环到的柱子矮的第一根柱子, 作为左右边界, 然后算面积, 取最大值

```java
/**
* 本参考程序来自九章算法，由 @Iris 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

public class Solution {
    /**作者: 千秋无痕
     * @param height: A list of integer
     * @return: The area of largest rectangle in the histogram
     */
    public int largestRectangleArea(int[] height) {
        // write your code here
        if (height == null || height.length == 0) {
            return 0;
        }
        if (height.length == 1) {
            return height[0];
        }
        
        int max = Integer.MIN_VALUE;
        int n = height.length;
        int l, r;
        
        for (int i = 0; i < n; ++i) {
            l = i;
            r = i;
            while (l - 1 >= 0 && height[l - 1] >= height[i]) {
                l--;
            }
            while (r + 1 <= n - 1 && height[r + 1] >= height[i]) {
                r++;
            }
            max = Math.max(max, (r - l + 1) * height[i]);
        }
        
        return max;
    }
}
```

**O(n^3)**

穷举左边界, 穷举右边界, 然后看左右边界之间最矮的柱子, 这根柱子将限制我们长方形的高.
