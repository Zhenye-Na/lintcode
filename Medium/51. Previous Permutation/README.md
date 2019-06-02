# 51. Previous Permutation

- **Description**
    - Given a list of integers, which denote a permutation.
    - Find the previous permutation in ascending order.
    - The list may contains duplicate integers.
- **Example**
    - For `[1,3,2,3]`, the previous permutation is `[1,2,3,3]`
    - For `[1,2,3,4]`, the previous permutation is `[4,3,2,1]`


## Solution

Related problem: **52. Next Permutation**

- 从后往前找“递增序列”，第一个不满足的标记为 **pivot**
- 从后往前找比 pivot 小的元素，将其与 **pivot** 交换位置
- 把从 **pivot** 之后的 重新排序 reverse


#### Python


```python
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # write your code here
        if not nums or len(nums) <= 1:
            return nums

        # Find longest non-decreasing suffix
        i = len(nums) - 1
        while i > 0 and nums[i - 1] <= nums[i]:
            i -= 1

        if i <= 0:
            list.reverse(nums)
            return nums

        pivot = i - 1

        # Find rightmost element that is below the pivot
        j = len(nums) - 1
        while nums[j] >= nums[pivot]:
            j -= 1

        # Swap the pivot with j
        nums[pivot], nums[j] = nums[j], nums[pivot]

        # Reverse the suffix
        nums[i:] = nums[len(nums) - 1 : pivot : -1]

        return nums

```
