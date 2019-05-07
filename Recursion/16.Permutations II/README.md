# 16. Permutations II

**Description**

Given a list of numbers with duplicate number in it. Find all unique permutations.

**Example**

Example 1:

```
Input: [1,1]
Output:
[
  [1,1]
]
```

Example 2:

```
Input: [1,2,2]
Output:
[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]
```

**Challenge**

Using recursion to do it is acceptable. If you can do it without recursion, that would be great!


**1. `itertools.permutations()`**

```python
import itertools
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        return list(set(itertools.permutations(nums)))
```


**2. Backtracking**


```python
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return [[]]

        nums.sort()
        visited = [False for _ in range(len(nums))]
        permutations = []
        self._find_permutations(nums, permutations, [], visited)
        return permutations

    def _find_permutations(self, nums, permutations, tmp, visited):
        if len(tmp) == len(nums):
            permutations.append(tmp[:])
            return

        for i in range(len(nums)):
            if not visited[i]:
                # remove duplicates
                if i > 0 and nums[i - 1] == nums[i] and visited[i - 1]:
                    continue

                # backtracking
                visited[i] = True
                tmp.append(nums[i])
                self._find_permutations(nums, permutations, tmp, visited)
                tmp.pop()
                visited[i] = False
```


首先对 array 进行排序，假如我们有这样一个排完序的数组 `[1,2,2]`，后面的 `2` 有可能会和 前面的 `2` 调换位置，但是结果是重复的，所以 追加一步操作 `i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]`，意思是：如果相邻两个元素相同，而且前面的没有使用过，那么我们就不能使用后面那个 `element`。


```java
public class Solution {
    /*
     * @param :  A list of integers
     * @return: A list of unique permutations
     */
    public List<List<Integer>> permuteUnique(int[] nums) {
        // write your code here
        List<List<Integer>> results = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            results.add(new ArrayList<Integer>());
            return results;
        }
        Arrays.sort(nums);
        helper(nums, new boolean[nums.length], new ArrayList<Integer>(), results);
        return results;
    }
    
    
    private void helper(int[] nums,
                        boolean[] visited,
                        List<Integer> permutation,
                        List<List<Integer>> results) {
        
        // Definition: Recursively find all unique permutations

        // Exit:
        if (permutation.size() == nums.length) {
            results.add(new ArrayList<>(permutation));
            return;
        }

        // Split:
        for (int i = 0; i < nums.length; i++) {

            if (visited[i] || ( i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]) ) {
                continue;
            }

            permutation.add(nums[i]);
            visited[i] = true;
            helper(nums, visited, permutation, results);
            permutation.remove(permutation.size() - 1);
            visited[i] = false;
        }

    }

}
```