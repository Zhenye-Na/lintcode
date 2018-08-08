public class Solution {
    /**
     * @param nums: An integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    public int longestIncreasingSubsequence(int[] nums) {
        // write your code here

        if (nums == null || nums.length == 0) {
            return 0;
        }

        // intialize an array filled with 1, because each integer is an increasing subsequence itself
        int[] arr = new int[nums.length];
        Arrays.fill(arr, 1);

        // DP
        // only update when nums[j] < nums[i] && arr[j] + 1 < arr[i]
        int length = nums.length;
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    arr[i] = Math.max(arr[j] + 1, arr[i]);
                }
            }
        }

        // find max in arr => LIS
        int size = 0;
        for (int idx = 0; idx < length; idx++) {
            if (arr[idx] > size) {
                size = arr[idx];
            }
        }

        return size;
    }


}







/**
* 本参考程序来自九章算法，由 @houweidong 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

public class Solution {
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    public int longestIncreasingSubsequence(int[] A) {
        int n = A.length;
        int[] f = new int[n];

        // If you remove comments in code, it can print out the longest sequence
        // 去掉所有加注释的地方可以打印方案

        // int[] pi = new int[n];
        //int p = 0;
        int max = 0;
        for (int i = 0; i < n; i++) {
            f[i] = 1;
            //pi[i] = -1;
            for (int j = 0; j < i; j++) {
                if (A[j] < A[i]) {
                    f[i] = f[i] > f[j] + 1 ? f[i] : f[j] + 1;
                    /*if (f[i] == f[j] + 1) {
                        pi[i] = j;
                    }*/
                }
            }
            if (f[i] > max) {
                max = f[i];
                //p = i;
            }
        }

        /*int[] seq = new int[max];
        for (int i = max - 1; i >= 0; --i) {
            seq[i] = A[p];
            p = pi[p];
        }

        for (int i = 0; i < max; ++i) {
            System.out.println(seq[i]);
        }*/
        return max;
    }
}
