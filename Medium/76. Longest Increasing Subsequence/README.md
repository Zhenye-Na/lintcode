# 76. Longest Increasing Subsequence

- **Description**
    - Given a sequence of integers, find the longest increasing subsequence (LIS).
    - You code should return the length of the LIS.
- **Clarification**
    - What's the definition of longest increasing subsequence?
    - The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.
    - https://en.wikipedia.org/wiki/Longest_increasing_subsequence
- **Example**
    - For `[5, 4, 1, 2, 3]`, the LIS is `[1, 2, 3]`, return `3`
    - For `[4, 2, 4, 5, 3, 7]`, the LIS is `[2, 4, 5, 7]`, return `4`
- **Challenge**
    - Time complexity `O(n^2)` or `O(nlogn)`


## Solution

### Dynamic Programming

因为看到了 Binary Search 的 tag 死也没想到这个题可以用 DP 做出来，**DP 需要多加练习，培养感觉!!**

这道题有几个很不错的讲解视频，列在下面，就不写解题思路了：

- [Tushar 的视频: Longest Increasing Subsequence](https://www.youtube.com/watch?v=CE2b_-XfVDk)
- [(Longest Increasing Subsequence) | GeeksforGeeks - YouTube](https://www.youtube.com/watch?v=Ns4LCeeOFS4)


```java
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
```


### Binary Search

因为这道题的 tag 是 Binary Search 所以点开的，没想到 Binary Search 只是基于 DP 的一个优化，整体思路没有太多变化，但是TM很巧妙啊！！！！

内容摘自 [StackOverflow](https://stackoverflow.com/questions/6129682/longest-increasing-subsequenceonlogn):

Let's first look at the n^2 algorithm:

```java
dp[0] = 1;
for( int i = 1; i < len; i++ ) {
   dp[i] = 1;
   for( int j = 0; j < i; j++ ) {   <-- improvement happens here
      if( array[i] > array[j] ) {
         if( dp[i] < dp[j]+1 ) {
            dp[i] = dp[j]+1;
         }
      }
   }
}
```

Now the improvement happens at the **second loop**, basically, you can improve the speed by using **binary search**. Besides the array `dp[]`, let's have another array `c[]`, `c` is pretty special, `c[i]` means: **the minimum value of the last element of the longest increasing sequence whose length is `i`**.

```java
sz = 1;
c[1] = array[0]; /*at this point, the minimum value of the last element of the size 1 increasing sequence must be array[0]*/
dp[0] = 1;
for( int i = 1; i < len; i++ ) {
   if( array[i] < c[1] ) {
      c[1] = array[i]; /*you have to update the minimum value right now*/
      dp[i] = 1;
   }
   else if( array[i] > c[sz] ) {
      c[sz+1] = array[i];
      dp[i] = sz+1;
      sz++;
   }
   else {
      int k = binary_search( c, sz, array[i] ); /*you want to find k so that c[k-1]<array[i]<c[k]*/
      c[k] = array[i];
      dp[i] = k;
   }
}
```

**具体解法@九章算法**


```java
/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
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
    public int longestIncreasingSubsequence(int[] nums) {
        int[] minLast = new int[nums.length + 1];
        minLast[0] = Integer.MIN_VALUE;
        for (int i = 1; i <= nums.length; i++) {
            minLast[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < nums.length; i++) {
            // find the first number in minLast >= nums[i]
            int index = binarySearch(minLast, nums[i]);
            minLast[index] = nums[i];
        }

        for (int i = nums.length; i >= 1; i--) {
            if (minLast[i] != Integer.MAX_VALUE) {
                return i;
            }
        }

        return 0;
    }

    // find the first number > num
    private int binarySearch(int[] minLast, int num) {
        int start = 0, end = minLast.length - 1;
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;
            if (minLast[mid] < num) {
                start = mid;
            } else {
                end = mid;
            }
        }

        return end;
    }
}

```


### 动态规划专题课：打印solution的版本

```java
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
```
