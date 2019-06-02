# 148. Sort Colors


- **Description**
    - Given an array with `n` objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
    - Here, we will use the integers `0`, `1`, and `2` to represent the color red, white, and blue respectively.
    - You are **not suppose to use the library's sort function** for this problem.
    - You should do it **in-place** (sort numbers in the original array).
- **Example**
    - Given `[1, 0, 1, 2]`, sort it in-place to `[0, 1, 1, 2]`.
- **Challenge**
    - A rather straight forward solution is a two-pass algorithm using **counting sort**.
    - First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
    - Could you come up with an one-pass algorithm using only constant space?



## Solution

**两根指针：**  
left 和 right, 两根指针，遇到 0 就把它放在 left 左边，如果遇到 2 就把它放在 right 右边。


```java
public class Solution {
    /**
     * @param nums: A list of integer which is 0, 1 or 2 
     * @return: nothing
     */
    public void sortColors(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return;
        }

        int left = 0, right = nums.length - 1, i = 0;

        while (i <= right) {
            if (nums[i] == 0) {
                swap(nums, left, i);
                left++;
                i++;
            } else if(nums[i] == 1) {
                i++;
            } else {
                swap(nums, right, i);
                right--;
            }
        }
    }

    private void swap(int[] nums, int left, int right) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }

}
```

**Counting Sort:**


```java
/**
* 本参考程序来自九章算法，由 @R同学 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

public class Solution {
    /**
     * @param nums: A list of integer which is 0, 1 or 2 
     * @return: nothing
     */
    public void sortColors(int[] nums) {
        // write your code here
        int red = 0;
        int blue = 0;
        int white = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                red++;
            }

            if (nums[i] == 1) {
                blue++;
            }

            if (nums[i] == 2) {
                white++;
            }
        }

        for (int i = 0; i < red; i++) {
            nums[i] = 0;
        }

        for (int i = red; i < red + blue; i++) {
            nums[i] = 1;
        }

        for (int i = red + blue; i < nums.length; i++) {
            nums[i] = 2;
        }
    }
}
```