# 100. Remove Duplicates from Sorted Array

**Description**


Given a sorted array, **remove** the duplicates in place such that each element appear only once and return the **new** length.

Do not allocate extra space for another array, you must do this **in place with constant memory**.


**Example**


Example 1:

```
Input:  []
Output: 0
```

Example 2:

```
Input:  [1,1,2]
Output: 2	
Explanation:  uniqued array: [1,2]
```


两个同向指针, 左指针用来"写", 右指针用来"读", 右指针遇到跟左指针不等的, 就把它"移"过来.

只需要返回长度即可, 不需要更改数组, 即不需要最后一步 `nums = nums[:new_length]`

Python 代码 (略繁琐)


```python
class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        length = len(nums)

        p1, p2 = 0, 1
        while p2 < length:
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
                p2 += 1
            else:
                while p2 < length and nums[p2] == nums[p1]:
                    p2 += 1
                if p2 < length:
                    p1 += 1
                    nums[p1] = nums[p2]
                    p2 += 1

        return p1 + 1

```


Java 代码

```java
public class Solution {
    /*
     * @param nums: An ineger array
     * @return: An integer
     */
    public int removeDuplicates(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int j = 0;
        int len = nums.length;
        for (int i = 1; i < len; i++) {
            if (nums[i] != nums[j]) {
                // update value
                j++;
                nums[j] = nums[i];
            }
        }
        return j + 1;
    }
}
```