# 183. Wood Cut


**Description**

Given `n` pieces of wood with length `L[i]` (integer array). Cut them into small pieces to guarantee you could have **equal or more than `k` pieces** with the same length. What is the longest length you can get from the `n` pieces of wood? Given `L` and `k`, return the maximum length of the small pieces.

> You couldn't cut wood into float length.

If you couldn't get `>= k` pieces, return `0`.


**Example**

Example 1

```
Input:
L = [232, 124, 456]
k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114cm long, however we can't cut it into 7 pieces if any piece is 115cm long.
```

Example 2

```
Input:
L = [1, 2, 3]
k = 7
Output: 0
Explanation: It is obvious we can't make it.
```

**Challenge**

`O(n log Len)`, where `Len` is the longest length of the wood.


**Binary Search**

- minimum length of wood segment is `1` and maximum length is `max(L)` - max element in all of the wood
- use a function to return the number of cuts (`num`) in the woods, compare it with `k`
- if `num >= k`, this means that length is small so that number of cuts is greater than `k` -> we can increase the wood cut length
- if `num < k`, this means there is no way to cut `k` parts using current length -> decrease length



```python
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L or not k or len(L) == 0:
            return 0

        start, end = 1, max(L)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._compute_k(L, mid) >= k:
                start = mid
            else:
                end = mid

        if self._compute_k(L, end) >= k:
            return end
        if self._compute_k(L, start) >= k:
            return start
        return 0


    def _compute_k(self, L, length):
        return sum([l // length for l in L])

```



```java
public class Solution {
    /**
     * @param L: Given n pieces of wood with length L[i]
     * @param k: An integer
     * @return: The maximum length of the small pieces
     */
    public int woodCut(int[] L, int k) {
        // write your code here
        if (L == null || L.length == 0) return 0;

        Arrays.sort(L);
        if (k == 0) return L[L.length - 1];
        int end = L[L.length - 1], start = 1;

        while (start + 1 < end) {

            int mid = (end - start) / 2 + start;
            int num = 0;

            for (int l : L) {
                num += (l / mid);

            }

            if (num >= k) {
                start = mid;
            } else if (num < k) {
                end = mid;
            }

        }

        int num = 0;
        int num2 = 0;
        for (int l : L) {
            num += (l / end);
            num2 += (l / start);
        }
        if (num >= k) {
            return end;
        } else if (num2 >= k) {
            return start;
        } else {
            return 0;
        }

    }
}
```
