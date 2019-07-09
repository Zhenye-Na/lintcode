# 507. Wiggle Sort II

**Description**

Given an *unsorted* array nums, reorder it such that

```
nums[0] < nums[1] > nums[2] < nums[3]....
```

- You may assume all input has valid answer.
- You just need to give one vaild answer.


**Example**

Example 1

```
Input: nums = [1, 5, 1, 1, 6, 4]
Output: [1, 4, 1, 5, 1, 6]
```

Example 2

```
Input: nums = [1, 3, 2, 2, 3, 1]
Output: [2, 3, 1, 3, 1, 2]
```

**Challenge**

Can you do it in `O(n)` time and/or in-place with `O(1)` extra space?


- Credit to @Jimmy 

分析

```
剛好這題沒有O(N)的python解 主要參考YiWang同學c的寫法
Time: O(N), Space: O(1)
首先先用find_kth找到median
接著設定兩個指針分別為even及odd 這裡用e跟o代替
然後我們會發現 wiggle sort
1.大於median的數值一定會放在odd的位置
2.小於median的數值一定會放在even的位置
所以o的起始位置為1, e的起始位置為最大index為偶數的位置
然後當i指針從0開始到n-1為止
如果發現nums[i] > median 且 i不在odd
＝＝就把nums[i]跟nums[odd]互換 odd += 2
或者發現nums[i] < median 且 i不在even
＝＝就把nums[i]跟nums[even]互換 even -= 2
但這個演算法仍然不正確,用下面的例子舉例：
[4,5,5,6], median=5
當i走完[4,5,5,6], 一個數值都不會換就輸出答案！
這是因為當我們忽略==median時
偶數位置0的數值4確實有 < median 而基數位置3的數值6確實有 > median
換句話說,只要我們能把e/i的位置,確實地放入小於/大於median的數值,就可以得到正確的答案

這時候我們就可以加上額外的條件
他的道理是
當我i > o的情況下
o的位置不一定是大於median的數,所以我把大於median的數放到本來o的位置,然後把o往後跳2
同理當我i < e的情況下
i的位置不一定是小於median的數,所以我把小於median的數放到本來e的位置,然後把i往前跳2
這時候就可以確實地把median分開
同樣的例子：
[4,5,5,6], median=5, i == 0, i < e -> swap
[5,5,4,6], median=5, i == 0, nums[i] == median -> i += 1
[5,5,4,6], median=5, i == 1, nums[i] == median -> i += 1
[5,5,4,6], median=5, i == 2, nums[i] < median, i == e (不滿足條件)-> i += 1
[5,5,4,6], median=5, i == 3, nums[i] > median, i > o (滿足條件) -> swap
[5,6,4,5], median=5, i == 3, nums[i] > median, i == o (不滿足條件)-> i += 1
i >= n - 1 -> 回傳nums
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
附上一個直覺, 要怎麼知道要把o放在1, e放在n-1/n-2? 如果把o放在n-1/n-2, e放在0會不會對？
答案是不會, 原因是當我們在find_kth的時候對nums做了partition, 所以所有小於median的數會在左邊, 大於在右邊
這時候把本來要存大於的o放在都是小於median的左邊, 把本來要存小於median的e放在都是大於median的右邊
就可以保證在swap的時候, 確實把小於median的數丟到e, 以及把大於median的數丟到o
不會換到錯的數!
```

```python
class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """

    def wiggleSort(self, nums):
        # write your code here
        median = self.findMedian(nums)
        n = len(nums)
        i = 0
        even, odd = n - 1 if (n - 1) % 2 == 0 else n - 2, 1

        while i < n:
            if nums[i] > median and (i % 2 != 1 or i > odd):
                nums[i], nums[odd] = nums[odd], nums[i]
                odd += 2
                continue

            if nums[i] < median and (i % 2 != 0 or even > i):
                nums[i], nums[even] = nums[even], nums[i]
                even -= 2
                continue

            i += 1

    def findMedian(self, nums):
        n = len(nums)
        if n % 2 == 0:
            return (self.findKth(nums, n // 2, 0, n - 1) + self.findKth(nums, n // 2 + 1, 0, n - 1)) / 2
        else:
            return self.findKth(nums, n // 2, 0, n - 1)

    def findKth(self, nums, k, start, end):
        if start == end:
            return nums[start]

        pivot = nums[(start + end) // 2]

        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start <= k - 1 <= right:
            return self.findKth(nums, k, start, right)
        elif left <= k - 1 <= end:
            return self.findKth(nums, k, left, end)
        else:
            return nums[k - 1]
```