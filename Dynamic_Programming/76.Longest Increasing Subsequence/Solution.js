/**
 * 本参考程序来自九章算法，由 @华助教 提供。版权所有，转发请注明出处。
 * - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
 * - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
 * - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
 * - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
 */

/**
 * @param nums: An integer array
 * @return: The length of LIS (longest increasing subsequence)
 */
const longestIncreasingSubsequence = function(nums) {
  var f = new Array(nums.length);
  var max = 0;
  var i, j;
  for (i = 0; i < nums.length; i++) {
    f[i] = 1;
    for (j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        f[i] = f[i] > f[j] + 1 ? f[i] : f[j] + 1;
      }
    }
    if (f[i] > max) {
      max = f[i];
    }
  }
  return max;
};
