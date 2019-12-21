# 791. Merge Number

**Description**

Given `n` numbers, now we need to merge `n` numbers into one number. And each time we can only select and merge two numbers `a`, `b`. Each merger needs to consume `a + b` energy. Output the *minimum energy* consumed by merging `n` numbers.

```
2 <= n <= 50000, the combined number will not exceed the int range
```

**Example**

Example 1:

```
Input:  [1,2,3,4]
Output:  19

Explanation:
Merge 1,2, which consumes 3 energy, and the rest is [3,4,3]. 
Then merge 3,3, which consumes 6 energy, and the rest is [6,4].
Then merge the last two numbers, which consumes 10 energy, and a total of 19 energy was consumed.
```

Example 2:

```
Input: [2,8,4,1]
Output:  25

Explanation:
Merge 1,2, which consumes 3 energy, and the rest is [8,4,3]. 
Merge 3,4, which consumes 7 energy, and the rest is [7,8]. 
Merge the last two numbers, which consumes 15 energy, 
and a total of 25 energy was consumed.
```

**Heap**

Priority Queue

```python
from heapq import heappush, heappop


class Solution:
    """
    @param numbers: the numbers
    @return: the minimum cost
    """
    def mergeNumber(self, numbers):
        # Write your code here
        if not numbers or len(numbers) == 0:
            return 0

        heap = []
        for num in numbers:
            heappush(heap, num)
        
        ans = 0
        while len(heap) >= 2:
            num1 = heappop(heap)
            num2 = heappop(heap)
            ans += num1 + num2
            heappush(heap, num1 + num2)

        return ans
```
