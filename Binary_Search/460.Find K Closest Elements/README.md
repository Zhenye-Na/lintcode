# 460. Find K Closest Elements

**Description**

Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

> The value k is a non-negative integer and will always be smaller than the length of the sorted array.  
> Length of the given array is positive and will not exceed $10^4$  
> Absolute value of elements in the array will not exceed $10^4$  
​​

**Example**

Example 1:

```
Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]
```

Example 2:

```
Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]
```

**Challenge**

`O(logn + k)` time


**投机取巧的解法**

按照列表每个元素跟 `target` 相差的绝对值排序原数组, 取出前 `k` 个即可

时间复杂度 `O(n)`

```python
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A or len(A) == 0:
            return None

        diff = [abs(e - target) for e in A]
        results = [a for _, a in sorted(zip(diff, A))]
        return results[:k]
```



**Binary Search + Two Pointers**

采用的是`二分法 + 双指针`  
二分法确定一个位置，左侧是 `< target`，右侧是 `>= target`  
然后用两根指针从中间向两边走，依次找到最接近的 `k` 个数


```python
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A or len(A) == 0:
            return None

        right = self._binary_search(A, target)
        if right == -1:
            return A[len(A) - k:][::-1]
        left = right - 1

        leftFlag, rightFlag = None, None
        results = []
        for _ in range(k):
            idx = self._compare(A, left, right, target)
            results.append(A[idx])
            if idx == left:
                if idx > 0:
                    left -= 1
                else:
                    leftFlag = True
                    break
            if idx == right:
                if idx < len(A) - 1:
                    right += 1
                else:
                    rightFlag = True
                    break

        if leftFlag:
            # move right pointer until k elements
            for num in range(len(results), k):
                results.append(A[right])
                right += 1

        if rightFlag:
            # move left pointer
            for num in range(len(results), k):
                results.append(A[left])
                left -= 1

        return results


    def _binary_search(self, A, target):
        """
        Find first position where A[position] >= target
        """
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                start = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return -1


    def _compare(self, A, leftIndex, rightIndex, target):
        if abs(A[leftIndex] - target) <= abs(A[rightIndex] - target):
            return leftIndex
        else:
            return rightIndex
```


@令狐冲 老师解法

注意点是: 找不到比他大的就返回 `end + 1` 不用返回 `-1`

```python
# 本参考程序来自九章算法, 由 @令狐冲 提供. 版权所有, 转发请注明出处.

class Solution2:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # 找到 A[left] < target, A[right] >= target
        # 也就是最接近 target 的两个数，他们肯定是相邻的
        right = self.find_upper_closest(A, target)
        left = right - 1
    
        # 两根指针从中间往两边扩展，依次找到最接近的 k 个数
        results = []
        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1
        
        return results
    
    def find_upper_closest(self, A, target):
        # find the first number >= target in A
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        
        if A[start] >= target:
            return start
        
        if A[end] >= target:
            return end
        
        # 找不到的情况
        return end + 1
        
    def is_left_closer(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target

```
