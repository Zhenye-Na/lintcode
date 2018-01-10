# 47. Majority Element II


- **Description**
    - Given an array of integers, the majority number is the number that occurs **`more than 1/3`** of the size of the array.
    - Find it.
    - There is only one majority number in the array.
- **Example**
    - Given `[1, 2, 1, 2, 1, 3, 3]`, return `1`.
- **Challenge**
    - `O(n)` time and `O(1)` extra space.


## Solution

### `O(n)` time and `O(n)` extra space

```python
class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        mapping = {}
        limit = len(nums) / 3

        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1

            if mapping[num] > limit:
                return num

```


### `O(n logn)` time and `O(1)` extra space

```python
class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        nums.sort()

        step = len(nums) / 3
        for idx, val in enumerate(nums):
            if val == nums[idx + step]:
                return val

```
