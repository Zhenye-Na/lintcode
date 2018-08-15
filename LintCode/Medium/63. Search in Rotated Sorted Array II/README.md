# 63. Search in Rotated Sorted Array II

- **Description**
    - Follow up for [**Search in Rotated Sorted Array**](https://github.com/Zhenye-Na/LxxxCode/tree/master/LintCode/Medium/62.%20Search%20in%20Rotated%20Sorted%20Array):
        - **What if duplicates are allowed?**
        - **Would this affect the run-time complexity? How and why?**
        - Write a function to determine if a given target is in the array.
- **Example**
    - Given `[1, 1, 0, 1, 1, 1]` and `target = 0`, return **`true`**.
    - Given `[1, 1, 1, 1, 1, 1]` and `target = 0`, return **`false`**.



## Solution


### Python

#### Version 1

Stack Overflow Question: [Fastest way to check if a value exist in a list](https://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exist-in-a-list)

![](https://i.stack.imgur.com/HSRgg.png)

```python
class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        # write your code here
        return target in set(A)
```


#### Version 2

```python
class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return False

        start, end = 0, len(A) - 1
        while (start + 1 < end):
            mid = (end + start) / 2

            if A[start] < A[mid]:
                if A[start] <= target and target <= A[mid]:
                    end = mid
                else:
                    start = mid
            elif A[start] < A[mid]:
                if A[end] >= target and A[mid] <= target:
                    start = mid
                else:
                    end = mid
            else:
                start += 1


        return True if A[start] == target or A[end] == target else False
```
