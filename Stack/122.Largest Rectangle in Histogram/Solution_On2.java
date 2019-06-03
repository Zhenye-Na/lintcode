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