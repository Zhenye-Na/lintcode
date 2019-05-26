# 153. Combination Sum II

**Description**

Given an array `num` and a number `target`. Find all unique combinations in `num` where the numbers sum to `target`.

```
1. Each number in num can only be used once in one combination.
2. All numbers (including target) will be positive integers.
3. Numbers in a combination a1, a2, ... , ak must be in non-descending order. (ie, a1 <= a2 <= ... <= ak)
4. Different combinations can be in any order.
5. The solution set must not contain duplicate combinations.
```

**Example**

Example 1:

```
Input: num = [7,1,2,5,1,6,10], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

Example 2:

```
Input: num = [1,1,1], target = 2
Output: [[1,1]]
Explanation: The solution set must not contain duplicate combinations.
```


```python
class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        self.results = []

        if not num or len(num) == 0:
            return self.results

        num.sort()
        self.target = target
        self.visited = [False for _ in range(len(num))]

        self._find_combination_sum_unique(num, [], 0)
        return self.results

    def _find_combination_sum_unique(self, num, tmp, start):
        if sum(tmp) == self.target:
            tmp2 = sorted(tmp)
            self.results.append(tmp2)
            return

        for i in range(start, len(num)):
            if sum(tmp) + num[i] > self.target:
                break

            if not self.visited[i]:

                # remove duplicates
                if i > 0 and num[i - 1] == num[i] and not self.visited[i - 1]:
                    continue

                self.visited[i] = True
                tmp.append(num[i])
                self._find_combination_sum_unique(num, tmp, i + 1)
                tmp.pop()
                self.visited[i] = False
```
