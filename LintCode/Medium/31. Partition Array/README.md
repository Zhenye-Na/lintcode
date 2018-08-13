# 31. Partition Array

- **Description**
    - Given an array `nums` of integers and an int k, partition the array (i.e move the elements in "`nums`") such that:
    - All elements **<** `k` are moved to the left
    - All elements **>=** `k` are moved to the right
    - Return the partitioning index, i.e the first index `i` `nums[i] >= k`.
- **Example**
    - If `nums = [3,2,2,1]` and `k=2`, a valid answer is `1`.
- **Challenge**
    - Can you partition the array in-place and in `O(n)`?
- **Notice**
    - You should do really partition in array `nums` instead of **just counting the numbers of integers smaller than `k`**.
    - If all elements in `nums` are smaller than k, then return `nums.length`

## Solution

两根指针，快排的一个步骤！很重要的思想

- 首指针去找 `>= k` 的第一个数
- 尾指针去找 `< k` 的倒数第一个数，找到了就交换过来
- 如此反复

可以注意到，相同的条件 使用了 4 次 `ps <= pe`， 基本都是这个 pattern


```java
public class Solution {
    /**
     * @param nums: The integer array you should partition
     * @param k: An integer
     * @return: The index after partition
     */
    public int partitionArray(int[] nums, int k) {
        // write your code here
        if (nums == null || nums.length == 0) return 0;

        int left = 0, right = nums.length - 1;

        while (left < right) {

            // find the number which is not supposed to be in the left
            while (left < right && nums[left] < k) {
                left++;
            }

            // find the number which is not supposed to be in the right
            while (left < right && nums[right] >= k) {
                right--;
            }

            // swap two elements
            if (left < right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
            }

        }

        if (nums[left] < k) {
            return left + 1;
        }

        return left;

    }
}
```


```java
public class Solution {
    /**
     * @param nums: The integer array you should partition
     * @param k: An integer
     * @return: The index after partition
     */
    public int partitionArray(int[] nums, int k) {
        // write your code here

        if (nums == null || nums.length == 0) {
            return 0;
        }

        int ps = 0, pe = nums.length - 1;
        while (ps <= pe) {

            while (ps <= pe && nums[pe] >= k) {
                pe--;
            }

            while (ps <= pe && nums[ps] < k) {
                ps++;
            }

            if (ps <= pe) {
                int tmp  = nums[ps];
                nums[ps] = nums[pe];
                nums[pe] = tmp;
                ps++;
                pe--;
            }
        }

        return ps;

    }
}
```
