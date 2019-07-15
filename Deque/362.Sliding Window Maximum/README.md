# 362. Sliding Window Maximum

**Description**

Given an array of `n` integer with duplicate number, and a moving window(size `k`), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.

**Example**

Example 1:

```
Input:
[1,2,7,7,8]
3
Output:
[7,7,8]

Explanation
At first the window is at the start of the array like this `[|1, 2, 7| ,7, 8]` , return the maximum `7`;
then the window move one step forward.`[1, |2, 7 ,7|, 8]`, return the maximum `7`;
then the window move one step forward again.`[1, 2, |7, 7, 8|]`, return the maximum `8`;
```

Example 2:

```
Input:
[1,2,3,1,2,3]
5
Output:
[3,3]

Explanation:
At first, the state of the window is as follows: ` [,2,3,1,2,1 | , 3] `, a maximum of ` 3 `;
And then the window to the right one. ` [1, | 2,3,1,2,3 |] `, a maximum of ` 3 `;
```

**Challenge**

`O(n)` time and `O(k)` memory


**单调递减队列**

比如 window size = 3, 数组 `[5, 2, 3, 4, 1, 6]`

`[5, 2, 3]` 中, 我们没有必要去存储 `2` 这个数字, 因为它永远都不可能称为最大值, 因为 `5`, `3` 都在.


```
quote @Nepenthes Athene 的解释

和官方答案一样。讲一下思路吧。
一开始上来考虑，能不能维护一个pair, 就记录当前最大值和index。
发现不能，因为轮到当前最大值被移除window后，我们没有备选的最大值，因为我们一直只记录了一个值。

所以我们需要一个数据结构来记录最大值和一些备选的值。
考虑到这个滑动窗口，有FIFO的特性，考虑用queue, python里的话直接用deque就很方便了。

deque里可以存（val, index)，也可以只存index

deque里的记录有两个特点：

存在于当前window
有可能成为下一个窗口的最大值。
第一个很好满足，就当 deque头部存的index 和 新来的index 差k时，证明它要出去了。

第二个可以反过来想，哪些值不能成为备选值呢？
比如值x, 当有新进deque的值y比x大时，x就一定不行。因为但凡x,y同窗，最大值永远不可能是x。
而且y比x后到，也会更晚出去。所以，x有生之年是不可能成为最大值了。
```

```python
from collections import deque


class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums or len(nums) == 0:
            return []

        max_queue, res = deque([]), []
        for i in range(len(nums)):

            while max_queue and nums[i] >= nums[max_queue[-1]]:
                max_queue.pop()
            max_queue.append(i)

            if i + 1 >= k:
                res.append(nums[max_queue[0]])

            if i + 1 - k == max_queue[0]:
                max_queue.popleft()

        return res
```

**huahua 的解法**

```python
"""
Author: Huahua
Running time: 238 ms
"""


class MaxQueue:
    def __init__(self):
        self.q_ = collections.deque()

    def push(self, e):
        while self.q_ and e > self.q_[-1]:
            self.q_.pop()
        self.q_.append(e)

    def pop(self):
        self.q_.popleft()

    def max(self):
        return self.q_[0]


class Solution:
    def maxSlidingWindow(self, nums, k):
        q = MaxQueue()
        ans = []
        for i in range(len(nums)):
            q.push(nums[i])
            if i >= k - 1:
                ans.append(q.max())
                if nums[i - k + 1] == q.max():
                    q.pop()
        return ans
```
