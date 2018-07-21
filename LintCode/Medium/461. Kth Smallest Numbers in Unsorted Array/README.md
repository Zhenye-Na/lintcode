# 461. Kth Smallest Numbers in Unsorted Array
Description
Find the kth smallest numbers in an unsorted integer array.

Example
Given [3, 4, 1, 2, 5], k = 3, the 3rd smallest numbers are [1, 2, 3].

Challenge
An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.


## Solution

**排序**

```java
public class Solution {
    /**
     * @param k: An integer
     * @param nums: An integer array
     * @return: kth smallest element
     */
    public int kthSmallest(int k, int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0 || nums.length < k) {
            return 0;
        }
        Arrays.sort(nums);
        return nums[k - 1];
        
    }
}
```

**Quick Select**


令狐老师小视频的模板代码.

- partition的**quick select**算法.
- 注意, 此题和quick sort有些不同.
- 如果`start == end`, 证明已经找到, `return nums[start]`即可.
- 如果`while`的判断是`left<=right`. 则有可能在partition后`right`和`left`之间有一个数.
- 因此, 我们要做出相应的判断和改变. partition后看三个区间.
    - 第一个区间是从`start`到`right`, 如果`k`在这个范围, 即`start + k - 1 <= right`, 继续在这个范围找k个数.
    - 第二个区间是从`left`到`end`, 如果`k`在这个范围, 即`start + k - 1 >= left`. 要在这个范围找`k-(left - start)`个数.
    - 或者`k`在`right`和`left`之间.这里面只有一个数, 那么`return nums[right + 1]`即可.
- 注意, 此题是找第`k`个小的数, 因此partition里要变换为`nums[left] < pivot`跳过, `nums[right] > pivot`跳过.


The algorithm is similar to QuickSort. The difference is, instead of recurring for both sides (after finding pivot), it recurs only for the part that contains the k-th smallest element. The logic is simple, if index of partitioned element is more than k, then we recur for left part. If index is same as k, we have found the k-th smallest element and we return. If index is less than k, then we recur for right part. This reduces the expected complexity from `O(n log n)` to `O(n)`, with a worst case of `O(n^2)`.


```java
/**
* 本参考程序来自九章算法，由 @y同学 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

public class Solution {
    /**
     * @param k: An integer
     * @param nums: An integer array
     * @return: kth smallest element
     */
    public int kthSmallest(int k, int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return -1;
        }
        
        return quickSelect(nums, 0, nums.length - 1, k);
    }
    
    private int quickSelect(int[] nums, int start, int end, int k) {
        if (start == end) {
            return nums[start];
        }
        
        int left = start;
        int right = end;
        int pivot = nums[(start + end) / 2];
        
        while (left <= right) {
            while (left <= right && nums[left] < pivot) {
                left++;
            }
            while (left <= right && nums[right] > pivot) {
                right--;
            }
            
            if (left <= right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                
                left++;
                right--;
            }
        }
        
        if (start + k - 1 <= right) {
            return quickSelect(nums, start, right, k);
        }
        
        if (start + k - 1 >= left) {
            return quickSelect(nums, left, end, k - (left - start));
        }
        
        return nums[right + 1];
    }
}
```

For more information about Quick Select, you can refer to this video


<a href="http://www.youtube.com/watch?feature=player_embedded&v=SXXpkdruLfc
" target="_blank"><img src="http://img.youtube.com/vi/SXXpkdruLfc/0.jpg" 
alt="Quickselect Algorithm with Partitioning | Code Tutorial" width="640" height="360" border="0" /></a>