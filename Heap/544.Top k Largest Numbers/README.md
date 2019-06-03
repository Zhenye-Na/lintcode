# 544. Top k Largest Numbers

**Description**

Given an integer array, find the top k largest numbers in it.

**Example**

Example 1

```
Input: [3, 10, 1000, -99, 4, 100] and k = 3
Output: [1000, 100, 10]
```

Example 2

```
Input: [8, 7, 6, 5, 4, 3, 2, 1] and k = 5
Output: [8, 7, 6, 5, 4]
```


**Quick Select**

```python
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        start = 0
        end = len(nums) - 1 
        index = self.partition(nums, start, end)

        while index != len(nums) - k:
            if index > len(nums) - k:
                end = index - 1 
                index = self.partition(nums, start, end)
            else:
                start = index + 1 
                index = self.partition(nums, start, end)

        result = nums[index:]
        result.sort()

        return result[::-1]
        
    def partition(self, A, start, end):
        index = start
        for i in range(start, end):
            if A[i] > A[end]:
                continue

            A[index], A[i] = A[i], A[index]
            index += 1 

        A[index], A[end] = A[end], A[index]
        return index
```

**Heap**

min heap

```java
// base on heap
class Solution {
    /*
     * @param nums an integer array
     * @param k an integer
     * @return the top k largest numbers in array
     */
    public int[] topk(int[] nums, int k) {
        PriorityQueue<Integer> minheap = new PriorityQueue<Integer> (k, new Comparator<Integer>() {
            public int compare(Integer o1, Integer o2) {
                return o1 - o2;
            }
        });

        for (int i: nums) {
            minheap.add(i);
            if (minheap.size() > k) {
                minheap.poll();
            }
        }

        int[] result = new int[k];
        for (int i = 0; i < result.length; i++) {
            result[k - i - 1] = minheap.poll();
        }
        return result;
    }
}
```

**heapq.nlargest()**

```python
import heapq

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        return heapq.nlargest(k, nums)
```