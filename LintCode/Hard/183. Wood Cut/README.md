# 183. Wood Cut

- **Description**
    - Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than `k` pieces with the same length. What is the longest length you can get from the `n` pieces of wood? Given `L & k`, return the maximum length of the small pieces.
    - You couldn't cut wood into float length.
    - If you couldn't get `>= k` pieces, return `0`.
- **Example**
    - For L=[232, 124, 456], k=7, return 114.
- **Challenge**
    - $O(n \log \text{Len})$, where `Len` is the longest length of the wood.


## Solution

### Python

```python
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if L is None or len(L) == 0:
            return 0

        start, end = 1, max(L)
        while (start + 1 < end):
            mid = (start + end) / 2

            count = self.counter(L, mid)
            if count >= k:
                start = mid
            else:
                end = mid

        count1, count2 = self.counter(L, start), self.counter(L, end)

        if count2 >= k:
            return end
        elif count1 >= k:
            return start
        else:
            return 0


    def counter(self, L, d):
        counter = 0
        for dist in L:
            counter += dist / d
        return counter
```

### Java

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
