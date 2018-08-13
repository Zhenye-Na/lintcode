# 57. 3Sum

**Description**
Given an array `S` of `n` integers, are there elements `a, b, c` in `S` such that `a + b + c = 0`?
Find **all unique triplets** in the array which gives the sum of zero.
Elements in a triplet `(a,b,c)` must be in **non-descending order**. (ie, `a ≤ b ≤ c`)
The solution set **must not contain duplicate triplets**.
**Example**
For example, given array `S = {-1 0 1 2 -1 -4}`, A solution set is:

```
(-1, 0, 1)
(-1, -1, 2)
```


## Solution


### **[Failed]** Binary Search + Two Pointers

先贴一个failed的代码，这道题是 Two Sum 的变体，第一反应想到的是 Two Pointers 肯定可以做，排好序之后代入即可，我用到了 Binary Search，我觉得这个方法肯定可以做，只是能力不足想不到好的 implementation 罢了。

failed 代码思路是这样的

- 首先排序，不然没办法判断多了还是少了
- 然后取出 头尾，在中间 Binary Search 一下，找到了就返回 index，找不到就返回 -1
- 然后就要移动 头尾指针，因为会有重复，所以有一个“象征性去重”的过程



```java
public class Solution {
    /**
     * @param numbers: Give an array numbers of n integer
     * @return: Find all unique triplets in the array which gives the sum of zero.
     */
    public List<List<Integer>> threeSum(int[] numbers) {
        // write your code here
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (numbers == null || numbers.length < 3) {
            return result;
        }

        Arrays.sort(numbers);
        int start = 0, end = numbers.length - 1;
        while (start < end) {
            List<Integer> combination = new ArrayList<>();

            int target = 0 - (numbers[start] + numbers[end]);
            int idx = binarySearch(numbers, target, start, end);

            if (idx != -1) {
                combination.add(numbers[start]);
                combination.add(numbers[idx]);
                combination.add(numbers[end]);
                result.add(combination);
                start++;
                while (start >= 0 && numbers[start] == numbers[start + 1]) {
                    start++;
                }
                end--;
                while (end <= numbers.length - 1 && numbers[end] == numbers[end - 1]) {
                    end--;
                }
            } else {
                if (-target < 0) {
                    start++;
                } else {
                    end--;
                }
            }
        }

        return result;
    }


    private int binarySearch(int[] nums, int target, int start, int end) {

        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;

            if (target == nums[mid]) {
                return mid;
            } else if (target < nums[mid]) {
                end = mid;
            } else {
                start = mid;
            }
        }

        if (target == nums[start]) {
            return start;
        }

        if (target == nums[end]) {
            return end;
        }

        return -1;
    }

}
```

Input

```
[-8,-8,-8,-5,-4,-1,-1,0,1,2,3,4,5,7]
```

Output

```
[[-8,1,7],[-8,3,5],         [-5,1,4],                            [-4,1,3],[-1,-1,2]]
```

Expected

```
[[-8,1,7],[-8,3,5],[-5,0,5],[-5,1,4],[-5,2,3],[-4,-1,5],[-4,0,4],[-4,1,3],[-1,-1,2],[-1,0,1]]
```

根据输出可以发现问题所在，以`-8`开头，`5`结尾的找到之后，会 `start++`，`end--`，然而 存在另一个仍然以`5`结尾的解，被程序直接跳过了

### 转化成 `Two Sum`

#### Java

```java
public class Solution {
    /**
     * @param numbers: Give an array numbers of n integer
     * @return: Find all unique triplets in the array which gives the sum of zero.
     */
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();

        if (nums == null || nums.length < 3) {
            return results;
        }

        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            // skip duplicate triples with the same first numebr
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1, right = nums.length - 1;
            int target = -nums[i];

            twoSum(nums, left, right, target, results);
        }

        return results;
    }

    public void twoSum(int[] nums,
                       int left,
                       int right,
                       int target,
                       List<List<Integer>> results) {
        while (left < right) {
            if (nums[left] + nums[right] == target) {
                ArrayList<Integer> triple = new ArrayList<>();
                triple.add(-target);
                triple.add(nums[left]);
                triple.add(nums[right]);
                results.add(triple);

                left++;
                right--;
                // skip duplicate pairs with the same left
                while (left < right && nums[left] == nums[left - 1]) {
                    left++;
                }
                // skip duplicate pairs with the same right
                while (left < right && nums[right] == nums[right + 1]) {
                    right--;
                }
            } else if (nums[left] + nums[right] < target) {
                left++;
            } else {
                right--;
            }
        }
    }
}
```

#### Python

```python
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        result = []
        numbers.sort()
        start, end = 0, len(numbers) - 1
        for index, elem in enumerate(numbers):

            # Remove duplicate elements in the front
            if (index > 0 and numbers[index - 1] == elem):
                continue

            start, end = index + 1, len(numbers) - 1
            while start < end:

                if (numbers[start] + numbers[end] + elem > 0):
                    end -= 1
                elif (numbers[start] + numbers[end] + elem < 0):
                    start += 1
                else:
                    # Append one possible combination
                    result.append([elem, numbers[start], numbers[end]])

                    # Move pointers
                    start += 1
                    end -= 1

                    # Remove duplicates
                    while (start < end and numbers[start] == numbers[start - 1]):
                        start += 1
                    while (start < end and numbers[end] == numbers[end + 1]):
                        end -= 1

        return result

```
