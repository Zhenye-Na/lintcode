# 48. Majority Number III

- **Description**
    - Given an array of integers and a number `k`, the majority number is the number that occurs **`more than 1/k`** of the size of the array.
    - Find it.
    - There is **only one majority number** in the array.
- **Example**
    - Given `[3,1,2,3,2,3,3,4,4,4]` and `k=3`, return `3`.
- **Challenge**
    - `O(n)` time and `O(k)` extra space


## Solution

### HashMap / dict {}


```python
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        limit = len(nums) / k
        dict = {}

        for num in nums:
            dict[num] = dict.get(num, 0) + 1

            if dict[num] > limit:
                return num

```
