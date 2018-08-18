46. Majority Element
Description
Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.

You may assume that the array is non-empty and the majority number always exist in the array.

Have you met this question in a real interview?  
Example
Given [1, 1, 1, 1, 2, 2, 2], return 1

Challenge
O(n) time and O(1) extra space


```
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
