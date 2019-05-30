# 373. Partition Array by Odd and Even

**Description**

Partition an integers array into odd number first and even number second.

```
The answer is not unique. All you have to do is give a vaild answer.
```

**Example**

Example 1:

```
Input: [1,2,3,4]
Output: [1,3,2,4]
```

Example 2:

```
Input: [1,4,2,3,5,6]
Output: [1,3,5,4,2,6]
```

**Challenge**

Do it in-place.

**Quick Select**

```python
class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return nums

        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and not self.isEven(nums[left]):
                left += 1
            while left <= right and self.isEven(nums[right]):
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums


    def isEven(self, num):
        return num % 2 == 0
```