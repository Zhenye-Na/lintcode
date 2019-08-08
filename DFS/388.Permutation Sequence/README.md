# 388. Permutation Sequence

**Description**

Given `n` and `k`, find the `k`th permutation of the dictionary order in the full permutation of `n`.

```
1 <= n <= 9
```

Example

Example 1:

```
Input: n = 3, k = 4
Output: "231"
Explanation:
For n = 3, all permutations are listed as follows:
"123", "132", "213", "231", "312", "321"
```

Example 2:

```
Input: n = 1, k = 1
Output: "1"
```

**Challenge**

`O(n*k)` in time complexity is easy, can you do it in `O(n^2)` or less?


**DFS**

```python
class Solution:
    """
    @param n: n
    @param k: the k th permutation
    @return: return the k-th permutation
    """
    def getPermutation(self, n, k):
        # write your code here
        nums = [str(i) for i in range(1, n + 1)]
        self.permutations = []
        self.dfs(nums, [])

        return self.permutations[k - 1]

    def dfs(self, nums, current):
        if len(current) == len(nums):
            self.permutations.append(''.join(current[:]))
            return

        for num in nums:
            if num not in current:
                current.append(num)
                self.dfs(nums, current)
                current.pop()
```

**Math**

```python
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param n: n
    @param k: the k-th permutation
    @return: the k-th permutation
    """

    def getPermutation(self, n, k):
        fac = [1]
        for i in range(1, n + 1):
            fac.append(fac[-1] * i)

        elegible = range(1, n + 1)
        per = []
        for i in range(n):
            digit = (k - 1) / fac[n - i - 1]
            per.append(elegible[digit])
            elegible.remove(elegible[digit])
            k = (k - 1) % fac[n - i - 1] + 1

        return "".join([str(x) for x in per])
```
