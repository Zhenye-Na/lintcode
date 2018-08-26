51. Previous Permutation
Description
Given a list of integers, which denote a permutation.

Find the previous permutation in ascending order.

The list may contains duplicate integers.

Have you met this question in a real interview?  
Example
For [1,3,2,3], the previous permutation is [1,2,3,3]

For [1,2,3,4], the previous permutation is [4,3,2,1]


## Solution

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
