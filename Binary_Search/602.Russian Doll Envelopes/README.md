# 602. Russian Doll Envelopes

**Description**

Give a number of envelopes with widths and heights given as a pair of integers `(w, h)`. One envelope can fit into another *if and only if* both the width and height of one envelope is *greater than* the width and height of the other envelope.

Find the *maximum* number of nested layers of envelopes.

**Example**

Example 1:

```
Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation:
the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
```

Example 2:

```
Input: [[4,5],[4,6],[6,7],[2,3],[1,1]]
Output: 4
Explanation: 
the maximum number of envelopes you can Russian doll is 4 ([1,1] => [2,3] => [4,5] / [4,6] => [6,7]).
```

**Related Problems**

https://www.lintcode.com/problem/longest-increasing-subsequence


**Binary Search**

先上答案 `O(nlogn)`

- 排序 O(nlogn)
- 循环 O(n)
- 二分 O(logn)


```python
from bisect import bisect_left

class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        if not envelopes or len(envelopes) == 0:
            return 0

        sorted_envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        
        lis, length = [0 for _ in range(len(envelopes))], 0
        for w, h in sorted_envelopes:
            idx = bisect_left(lis, h, 0, length)
            lis[idx] = h

            if idx == length:
                length += 1

        return length
```

在这个做法之前想到用 heap, 但是后来发现 heap 是可以简化排序这个方法, pop 出来的都是当前 w 最小的, 有可能 w 最小的信封, h 巨大无比, 所以这个信封没什么用但是仍然考虑了. 弃之

最让我恍然大悟的是看到答案区大佬的讲解才发现为什么题目旁边明明白白的写着跟 LIS Related. 真的是自己想了半天没看出来

在这里引用一下解法以及解析

```
原作者: Roger @ 九章

envelopes 先按 w 升序排序，再按 h 降序 排序，
只需考虑 h 即可, 因为 w 已经升序排列好, 因为 h 大的在前, 所以相同的 w 下的不同 h, 只会选择最大的那个 h

就可以将问题转换为 h 的 Longest Increasing subSequence

follow up:
信封可以旋转，怎么求最长序列？

答案:
先做预处理，例如对于信封 <3, 4>，把旋转之后的信封 <4, 3> 也加入到原数组中, 再按照本题的方法进行求解
```


**Dynamic Programming**







