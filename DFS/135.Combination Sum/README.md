# 135. Combination Sum

**Description**

Given a set of candidtate numbers `candidates` and a target number `target`. Find all unique combinations in `candidates` where the numbers sums to `target`.

The **same** repeated number may be chosen from `candidates` **unlimited number of times**.

```
1. All numbers (including target) will be positive integers.
2. Numbers in a combination a1, a2, ... , ak must be in non-descending order. (ie, a1 <= a2 <= ... <= ak)
3. Different combinations can be in any order.
4. The solution set must not contain duplicate combinations.
```

**Example**

Example 1:

```
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]
```

Example 2:

```
Input: candidates = [1], target = 3
Output: [[1, 1, 1]]
```


**Solution 1**

每次循环递减 `target`, 如果发现 `target` 变成了 `0`. 那么就是找到了一组. 每一个数可以用很多次, 所以内层循环开始位置不是 `i + 1` 而是 `i` .

```python
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results

    def dfs(self, candidates, target, start, combination, results):
        if target == 0:
            # deepcooy
            return results.append(list(combination))
            
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            
            # [2] => [2,2]
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            # [2,2] => [2]
            combination.pop()   # backtracking
```



**Solution 2**

DFS：

- 先把list排序
- 调用DFS，依次把数组里的元素往集合里放，放一个减一次
- target == 0 时返回
- 把去重放在了dfs函数里，当然在主程序里先去一遍重也没毛病。

```python
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates or len(candidates) == 0:
            return [[]]

        candidates.sort()
        self.results = []
        self.target = target
        visited = [False for _ in range(len(candidates))]
        self._find_combination_sum(candidates, [], visited, 0)
        return self.results

    def _find_combination_sum(self, candidates, current_combination, visited, start):
        if sum(current_combination) == self.target:
            current_combination.sort()
            self.results.append(current_combination[:])
            return

        for i in range(start, len(candidates)):
            if sum(current_combination) + candidates[i] > self.target:
                break

            if i > 0 and candidates[i - 1] == candidates[i] and not visited[i - 1]:
                continue

            current_combination.append(candidates[i])
            visited[i] = True
            self._find_combination_sum(candidates, current_combination, visited, i)
            current_combination.pop()
            visited[i] = False
```