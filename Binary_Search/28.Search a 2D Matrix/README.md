# 28. Search a 2D Matrix


**Description**

Write an efficient algorithm that searches for a value in an `m x n` matrix.

This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.


**Example**

```
Example 1:
	Input:  [[5]],2
	Output: false
	
	Explanation: 
	false if not included.
	
Example 2:
	Input:  [
				[1, 3, 5, 7],
				[10, 11, 16, 20],
				[23, 30, 34, 50]
			],3
	Output: true
	
	Explanation: 
	return true if included.
```

**Challenge**

`O(log(n) + log(m))` time


### One pass Binary Search

```python
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or target is None:
            return False

        flat_matrix = [item for row in matrix for item in row]

        start, end = 0, len(flat_matrix) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if flat_matrix[mid] == target:
                return True
            elif flat_matrix[mid] < target:
                start = mid
            else:
                end = mid


        if flat_matrix[start] == target or flat_matrix[end] == target:
            return True
        else:
            return False

```


### Two pass Binary Search

```python
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return -1

        # Binary Search on first column
        first_col = [row[0] for row in matrix]
        indicator, found = self._binary_search_on_col(first_col, target)

        # Binary Search on row if needed
        if found:
            return True
        else:
            return self._binary_search_on_row(matrix[indicator], target)

    def _binary_search_on_col(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return -1, True
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[start] > target:
            return start - 1, False
        if nums[end] > target:
            return end - 1, False
        else:
            return end, False

    def _binary_search_on_row(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        return True if nums[start] == target or nums[end] == target else False
       
```