# 894. Pancake Sorting

**Description**

Given an unsorted array, sort the given array. You are allowed to do only following operation on array.

- `flip(arr, i)`: Reverse array from `0` to `i` 
- Unlike a traditional sorting algorithm, which attempts to sort with the fewest comparisons possible, the goal is to sort the sequence in as few reversals as possible.
- You only call `flip` function.
- Don't allow to use any sort function or other sort methods.


```
Java: you can call FlipTool.flip(arr, i)
C++: you can call FlipTool::flip(arr, i)
Python 2&3: you can call FlipTool.flip(arr, i)
```

**Example**

Example 1:

```
Input: array = [6,11,10,12,7,23,20]
```


Example 2:

```
Input: array = [4, 2, 3]
Explanation:
	flip(array, 2)
	flip(array, 1)	
```

从后往前, 找数组中的最大值所在index 先把 array[:max_idx] flip 一次, 再把整体 flip 最大值就跑到最后了, 然后再把指针往做移动

```python
class Solution:
    """
    @param array: an integer array
    @return: nothing
    """
    def pancakeSort(self, array):
        # Write your code here
        if not array or len(array) == 0:
            return

        n = len(array)
        for i in range(n - 1, -1, -1):
            max_idx = self.findMax(array[: i + 1])
            if max_idx != i:
                FlipTool.flip(array, max_idx)
                FlipTool.flip(array, i)

    def findMax(self, array):
        max_num, max_idx = - sys.maxsize, -1
        for i in range(len(array)):
            if array[i] > max_num:
                max_idx = i
                max_num = array[i]

        return max_idx
```
