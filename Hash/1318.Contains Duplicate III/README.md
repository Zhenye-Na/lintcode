# 1318. Contains Duplicate III

**Description**

Given an array of integers, find out whether there are two distinct indices `i` and `j` in the array such that the absolute difference between `nums[i]` and `nums[j]` is at most `t` and the absolute difference between `i` and `j` is at most `k`.

**Example**

Example 1

```
Input: nums = [1,3,1], k = 1, t = 1
Output: false
Explanation: 
nums[2] = 1, nums[1] = 3, nums[1] - nums[2] = 2 > t
nums[0] = 1, nums[2] = 1, nums[1] - nums[2] = 0 < t,
2 - 0 = 2 > k
```

Example 2

```
Input: nums = [1,3,1], k = 1, t = 2
Output: true
Explanation: 
nums[2] = 1, nums[1] = 3, nums[1] - nums[2] = 2 = t,
2 - 1 = 1 = k
```

**Two pointers + Hash Table**

`right <= min(left + k, len(nums) + 1)`

```python
# 本参考程序来自九章算法，由 @J同学 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @param t: the given t
    @return: whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
    """
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # Write your code here
        i = j = 0
        nearby = {}
        n = len(nums)

        while i < n:
            while j < min(i + k + 1, n):
                for m in range(nums[j] - abs(t), nums[j] + abs(t) + 1):
                    if m in nearby:
                        return True

                nearby[nums[j]] = nearby.get(nums[j], 0) + 1
                j += 1

            nearby[nums[i]] -= 1
            if nearby[nums[i]] == 0:
                del nearby[nums[i]]

            i += 1

        return False
```


**Deque**

89% TLE 过不了

```python
from collections import deque

class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @param t: the given t
    @return: whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
    """
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # Write your code here
        if not nums or len(nums) == 0 or k <= 0:
            return False

        record = deque([])
        for i in range(k + 1):

            for target in range(nums[i] - t, nums[i] + t + 1):
                if target in record:
                    return True

            record.append(nums[i])

        for j in range(k + 1, len(nums)):
            record.popleft()
            for target in range(nums[j] - t, nums[j] + t + 1):
                if target in record:
                    return True 

            record.append(nums[j])

        return False
```