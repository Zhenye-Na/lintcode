# 17. Subsets

- **Description**
    - Given a set of distinct integers, return all possible subsets.
    - Elements in a subset must be in **non-descending** order.
    - The solution set must not contain duplicate subsets.
- **Example**
- If S = [1,2,3], a solution is:

    ```c
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
    ```

- **Challenge**
    - Can you do it in both recursively and iteratively?


## Solution

### Backtracking

```java
public class Solution {
    /**
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    public List<List<Integer>> subsets(int[] nums) {
        // write your code here
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        helper(nums, result, new ArrayList<Integer>(), 0);
        return result;
    }

    public void helper(int[] nums, List<List<Integer>> res, List<Integer> cur, int start) {
        List<Integer> subset = new ArrayList<>(cur);
        res.add(subset);

        // DFS
        for (int i = start; i <= nums.length - 1; i += 1) {
            cur.add(nums[i]);
            helper(nums, res, cur, i + 1);
            cur.remove(cur.size() - 1);
        }

    }

}
```
