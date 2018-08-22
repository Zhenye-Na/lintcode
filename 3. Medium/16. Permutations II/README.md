# 16. Permutations II

- **Description**
    - Given a list of numbers with duplicate number in it. Find all **unique** permutations.
- **Example**
    - For numbers `[1,2,2]` the unique permutations are:

    ```java
    [
      [1,2,2],
      [2,1,2],
      [2,2,1]
    ]
    ```

- **Challenge**
    - Using recursion to do it is acceptable. If you can do it without recursion, that would be great!


## Solution

1. 是 `15. Permutation` 的 followup question，题目要求去重，首先想到用HashSet去重，代码如下：

缺点：太TMD慢了，做了很多冗余工作

### Code

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
        
        helper(nums, new boolean[nums.length], new ArrayList<Integer>(), results);
        
        Set<List<Integer>> hs = new HashSet<>();
        hs.addAll(results);
        results.clear();
        results.addAll(hs);
        return results;
    }
    
    private void helper(int[] nums,
                        boolean[] visited,
                        List<Integer> permutation,
                        List<List<Integer>> results) {
        
        // Definition: recursively permutate array

        // Exit:
        if (permutation.size() == nums.length) {
            results.add(new ArrayList<Integer>(permutation));
            return;
        }


        // Split:
        for (int i = 0; i < nums.length; i++) {
            if (!visited[i]) {
                permutation.add(nums[i]);
                visited[i] = true;
                helper(nums, visited, permutation, results);
                permutation.remove(permutation.size() - 1);
                visited[i] = false;
            }

        }
        
    }
};
```

2. 第二种方法会快一点。思路基本一样，只不过要调整 helper function 里的判断条件。

    首先对 array 进行排序，这一步在 solution 1 省略了。假如我们有这样一个排完序的数组 `[1,2,2]`，后面的 `2` 有可能会和 前面的 `2` 调换位置，但是结果是重复的，所以 追加一步操作 `i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]`，意思是：如果相邻两个元素相同，而且前面的没有使用过，那么我们就不能使用后面那个 `element`。


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