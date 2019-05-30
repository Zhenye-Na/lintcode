# 56. Two Sum

**Description**

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where `index1` must be less than `index2`. Please note that your returned answers (both `index1` and `index2`) are zero-based.

You may assume that each input would have exactly one solution

**Example**

Example 1:

```
numbers=[2, 7, 11, 15], target=9
return [0, 1]
```

Example 2:

```
numbers=[15, 2, 7, 11], target=9
return [1, 2]
```

**Challenge**

Either of the following solutions are acceptable:

- `O(n)` Space, `O(nlogn)` Time
- `O(n)` Space, `O(n)` Time


**Two Pointers**

要返回的是原数组的 index 而不是排序之后的数组

所以 `argsort` 一下原数组, 获取到排序后原数组的 index

然后正常排序做

```python
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if not numbers or len(numbers) < 2:
            return [-1, -1]

        arg_nums = [x for x, y in sorted(enumerate(numbers), key = lambda x: x[1])]
        numbers.sort()
        left, right = 0, len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return sorted([arg_nums[left], arg_nums[right]])
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]
```

**HashMap**

```python
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

class Solution(object):
    def twoSum(self, nums, target):
        # hash用于建立数值到下标的映射
        hash = {}
        # 循环 nums 数值，并添加映射
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i
        # 无解的情况
        return [-1, -1]
```
