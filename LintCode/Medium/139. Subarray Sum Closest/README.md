# 139. Subarray Sum Closest

- **Description**
    - Given an integer array, find a subarray with sum closest to zero.
    - Return the indexes of the first number and last number.
- **Example**
    - Given `[-3, 1, 1, -3, 5]`, return `[0, 2]`, `[1, 3]`, `[1, 1]`, `[2, 2]` or `[0, 4]`.
- **Challenge**
    - `O(nlogn)` time



## Solution

### **[Failed]** 暴力解法 O(n^2)

```java
class ResultType {
    int bestSum;
    int[] combination;
    public ResultType(int s, int[] c) {
        bestSum = s;
        combination = c;
    }
}


public class Solution {
    /*
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number and the index of the last number
     */
    public int[] subarraySumClosest(int[] nums) {
        // write your code here
        if (nums == null || nums.length < 2) {
            return new int[]{0, 0};
        }

        ResultType resultType = new ResultType(Integer.MAX_VALUE, new int[]{0, 0});

        int sum = nums[0] + nums[1];
        int length = nums.length;
        for (int i = 0; i < length; i++) {
            for (int j = i + 1; j < length; j++) {
                int currSum = nums[i] + nums[j];
                if (Math.abs(currSum) < Math.abs(resultType.bestSum)) {
                    resultType.bestSum = currSum;
                    resultType.combination = new int[]{i, j};
                }
            }
        }

        return resultType.combination;
    }
}
```

### Prefix Sum 前缀和数组

**问：** 为什么需要一个 (0,0) 的初始 Pair?

**答：**

```
我们首先需要回顾一下，在 subarray 这节课里，我们讲过一个重要的知识点，叫做 Prefix Sum
比如对于数组 [1,2,3,4]，他的 Prefix Sum 是 [1,3,6,10]
分别表示 前1个数之和，前2个数之和，前3个数之和，前4个数之和
这个时候如果你想要知道 子数组 从下标 1 到下标 2 的这一段的和(2+3)，就用前 3个数之和 减去 前1个数之和 = PrefixSum[2] - PrefixSum[0] = 6 - 1 = 5
你可以看到这里的 前 x 个数，和具体对应的下标之间，存在 +-1 的问题
第 x 个数的下标是 x - 1，反之下标 x 是第 x + 1 个数
那么问题来了，如果要计算 下标从 0~2 这一段呢？也就是第1个数到第3个数，因为那样会访问到 PrefixSum[-1]
所以我们把 PrefixSum 整体往后面移动一位，把第0位空出来表示前0个数之和，也就是0. => [0,1,3,6,10]
那么此时就用 PrefixSum[3] - PrefixSum[0] ，这样计算就更方便了。
此时，PrefixSum[i] 代表 前i个数之和，也就是 下标区间在 0 ~ i-1 这一段的和

那么回过头来看看，为什么我们需要一个 (0,0) 的 pair 呢？
因为 这个 0,0 代表的就是前0个数之和为0
一个 n 个数的数组， 变成了 prefix Sum 数组之后，会多一个数出来
```


```java
/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

class Pair {
    int sum;
    int index;
    public Pair(int s, int i) {
        sum = s;
        index = i;
    }
}


public class Solution {
    /*
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number and the index of the last number
     */
    public int[] subarraySumClosest(int[] nums) {
        // write your code here
        int[] res = new int[2];
        if (nums == null || nums.length == 0) {
            return res;
        }

        int len = nums.length;
        if(len == 1) {
            res[0] = res[1] = 0;
            return res;
        }

        Pair[] sums = new Pair[len+1];
        int prev = 0;
        sums[0] = new Pair(0, 0);

        for (int i = 1; i <= len; i++) {
            sums[i] = new Pair(prev + nums[i-1], i);
            prev = sums[i].sum;
        }

        Arrays.sort(sums, new Comparator<Pair>() {
           public int compare(Pair a, Pair b) {
               return a.sum - b.sum;
           }
        });

        int ans = Integer.MAX_VALUE;
        for (int i = 1; i <= len; i++) {

            if (ans > sums[i].sum - sums[i-1].sum) {
                ans = sums[i].sum - sums[i-1].sum;
                int[] temp = new int[]{sums[i].index - 1, sums[i - 1].index - 1};
                Arrays.sort(temp);
                res[0] = temp[0] + 1;
                res[1] = temp[1];
            }
        }

        return res;

    }
}
```



## Find the Sub-array with sum closest to 0

Given an array of both positive and negative numbers, the task is to find out the subarray whose sum is closest to 0.
There can be multiple such subarrays, we need to output just 1 of them.

**Examples**:

```
Input : arr[] = {-1, 3, 2, -5, 4}
Output : 1, 3
Subarray from index 1 to 3 has sum closest to 0 i.e.
3 + 2 + -5 = 0
```

```
Input : {2, -5, 4, -6, 3}
Output : 0, 2
2 + -5 + 4 = 1 closest to 0
Asked in : Microsoft
```


1. A Naive approach is to consider all subarrays one by one and update indexes of subarray with sum closest to 0.

```c++
// C++ program to find subarray with sum closest to 0

#include <bits/stdc++.h>
using namespace std;

// Function to find the subarray
pair<int, int> findSubArray(int arr[], int n)
{

    int start, end, min_sum = INT_MAX;

    // Pick a starting point
    for (int i = 0; i < n; i++) {

        // Consider current starting point
        // as a subarray and update minimum
        // sum and subarray indexes
        int curr_sum = arr[i];
        if (min_sum > abs(curr_sum)) {
            min_sum = abs(curr_sum);
            start = i;
            end = i;
        }

        // Try all subarrays starting with i
        for (int j = i + 1; j < n; j++) {
            curr_sum = curr_sum + arr[j];

            // update minimum sum
            // and subarray indexes
            if (min_sum > abs(curr_sum)) {
                min_sum = abs(curr_sum);
                start = i;
                end = j;
            }
        }
    }

    // Return starting and ending indexes
    pair<int, int> p = make_pair(start, end);
    return p;
}

// Drivers code
int main()
{
    int arr[] = { 2, -5, 4, -6, -3 };
    int n = sizeof(arr) / sizeof(arr[0]);

    pair<int, int> point = findSubArray(arr, n);
    cout << "Subarray starting from ";
    cout << point.first << " to " << point.second;
    return 0;
}
```

Time Complexity: $O(n^2)$


2. An Efficient method is to perform following steps:

- Maintain a Prefix sum array . Also maintain indexes in the prefix sum array.
- Sort the prefix sum array on the basis of sum.
- Find the two elements in a prefix sum array with minimum difference.
- i.e.  Find `min(pre_sum[i] - pre_sum[i-1])`
- Return indexes of pre_sum with minimum difference.
- Subarray with `(lower_index+1, upper_index)` will have the sum closest to 0.
- Taking `lower_index+1` because on subtracting value at `lower_index` we get the sum closest to 0. That’s why `lower_index` need not to be included.


```c++
// C++ program to find subarray with sum closest to 0

#include <bits/stdc++.h>
using namespace std;

struct prefix {
    int sum;
    int index;
};

// Sort on the basis of sum
bool comparison(prefix a, prefix b)
{
    return a.sum < b.sum;
}

// Returns subarray with sum closest to 0.
pair<int, int> findSubArray(int arr[], int n)
{
    int start, end, min_diff = INT_MAX;

    prefix pre_sum[n + 1];

    // To consider the case of subarray starting
    // from beginning of the array
    pre_sum[0].sum = 0;
    pre_sum[0].index = -1;

    // Store prefix sum with index
    for (int i = 1; i <= n; i++) {
        pre_sum[i].sum = pre_sum[i-1].sum + arr[i-1];
        pre_sum[i].index = i - 1;
    }

    // Sort on the basis of sum
    sort(pre_sum, pre_sum + (n + 1), comparison);

    // Find two consecutive elements with minimum difference
    for (int i = 1; i <= n; i++) {
        int diff = pre_sum[i].sum - pre_sum[i-1].sum;

        // Update minimum difference
        // and starting and ending indexes
        if (min_diff > diff) {
            min_diff = diff;
            start = pre_sum[i-1].index;
            end = pre_sum[i].index;
        }
    }

    // Return starting and ending indexes
    pair<int, int> p = make_pair(start + 1, end);
    return p;
}

// Drivers code
int main()
{
    int arr[] = { 2, 3, -4, -1, 6 };
    int n = sizeof(arr) / sizeof(arr[0]);

    pair<int, int> point = findSubArray(arr, n);
    cout << "Subarray starting from ";
    cout << point.first << " to " << point.second;

    return 0;
}
```

Time Complexity: $O(n \log n)$


**Reference: **
[https://www.careercup.com/question?id=14583859](https://www.careercup.com/question?id=14583859)
