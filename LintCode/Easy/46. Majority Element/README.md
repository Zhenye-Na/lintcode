# 46. Majority Element

- **Description**
    - Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.
    - You may assume that the array is non-empty and the majority number always exist in the array.
- **Example**
    - Given `[1, 1, 1, 1, 2, 2, 2]`, return `1`
- **Challenge**
    - `O(n)` time and `O(1)` extra space

## Solution

### HashMap / dict {}

`O(n)` time and `O(n)` extra space

#### Python

```python
class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
```

### Misra-Gries Family of Algorithms - MAJORITY problem

`O(n)` time and `O(1)` extra space

Let us look at the **MAJORITY** problem first. We have two variables that we store. The **first-variable is the key** (which is either a member of `1,2,…,m` or a `null-entity`). The **second-variable is an integer** (which is a count). We start with an empty key, and a count of zero.

Every time an element `a_i = j` of the data-stream is observed,

- If the key is `empty` we set the value of the key to `j`, and we initialize the count to `1`.
- If the key is `not empty`, and equal to `j`, we increment the count by `1`.
- If the key is `not empty`, and not equal to `j`, we decrement the count by `1`
- If the count becomes zero as a result of this decrementing, we set the key to `null-entity`.

It is not hard to see that if there is a majority-element, it will be the value of the key.

```python
class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        key, count = None, 0
        for num in nums:
            if key is None:
                key, count = num, 1
            else:
                if key == num:
                    count += 1
                else:
                    count -= 1

            if count == 0:
                key = None

        return key
```
